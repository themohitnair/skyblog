package fileops

import (
	"fmt"
	"os"
	"path/filepath"
	"time"

	"github.com/russross/blackfriday/v2"
	"gopkg.in/yaml.v3"
)

type BlogMetadata struct {
	Author string    `yaml:"author"`
	Title  string    `yaml:"title"`
	Date   time.Time `yaml:"date"`
}

func TraverseBlogs() []string {
	files, err := os.ReadDir("./blogs")
	if err != nil {
		fmt.Println("Error reading directory:", err)
		return nil
	}

	var blogDirs []string

	for _, file := range files {
		if file.IsDir() {
			blogDirs = append(blogDirs, file.Name())
		}
	}
	return blogDirs
}

func ReadBlogMetadataYaml(dirPath string) (*BlogMetadata, error) {
	yamlFilePath := fmt.Sprintf("%s/metadata.yaml", dirPath)

	file, err := os.Open(yamlFilePath)
	if err != nil {
		return nil, fmt.Errorf("error opening YAML file: %w", err)
	}
	defer file.Close()

	var metadata BlogMetadata

	decoder := yaml.NewDecoder(file)
	err = decoder.Decode(&metadata)
	if err != nil {
		return nil, fmt.Errorf("error decoding YAML: %w", err)
	}

	return &metadata, nil
}

func MarkdownContentToHTML(dirPath string) (string, error) {
	mdFilePath := filepath.Join(dirPath, "content.md")

	mdContent, err := os.ReadFile(mdFilePath)
	if err != nil {
		return "", fmt.Errorf("error reading Markdown file: %w", err)
	}

	htmlContent := blackfriday.Run(mdContent)

	return string(htmlContent), nil
}

func GetAllBlogMetadata() ([]BlogMetadata, error) {
	var allMetadata []BlogMetadata

	blogDirs := TraverseBlogs()
	if blogDirs == nil {
		return nil, fmt.Errorf("error retrieving blog directories")
	}

	for _, dir := range blogDirs {
		dirPath := filepath.Join("./blogs", dir)
		metadata, err := ReadBlogMetadataYaml(dirPath)
		if err != nil {
			fmt.Printf("Error reading metadata for %s: %v\n", dir, err)
			continue
		}
		allMetadata = append(allMetadata, *metadata)
	}

	return allMetadata, nil
}
