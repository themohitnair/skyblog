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
	Author        string    `yaml:"author"`
	Title         string    `yaml:"title"`
	Date          time.Time `yaml:"date"`
	DirectoryName string    `yaml:"-"`
}

func ParseDate(dateStr string) (time.Time, error) {
	layout := "January 2, 2006 15:04 -0700 MST"
	return time.Parse(layout, dateStr)
}

func ReadBlogMetadataYaml(dirPath string, dirName string) (BlogMetadata, error) {
	var metadata BlogMetadata

	filePath := fmt.Sprintf("%s/metadata.yaml", dirPath)
	data, err := os.ReadFile(filePath)
	if err != nil {
		return metadata, err
	}

	temp := struct {
		Author string `yaml:"author"`
		Title  string `yaml:"title"`
		Date   string `yaml:"date"`
	}{}
	if err := yaml.Unmarshal(data, &temp); err != nil {
		return metadata, err
	}

	parsedDate, err := ParseDate(temp.Date)
	if err != nil {
		return metadata, err
	}

	metadata = BlogMetadata{
		Author:        temp.Author,
		Title:         temp.Title,
		Date:          parsedDate,
		DirectoryName: dirName,
	}

	return metadata, nil
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
		metadata, err := ReadBlogMetadataYaml(dirPath, dir)
		if err != nil {
			fmt.Printf("Error reading metadata for %s: %v\n", dir, err)
			continue
		}
		allMetadata = append(allMetadata, metadata)
	}

	return allMetadata, nil
}
