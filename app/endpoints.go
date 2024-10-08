package app

import (
	"fmt"
	"html/template"
	"os"
	"skyblog/fileops"
	"strings"

	"github.com/gin-gonic/gin"
)

func contains(slice []string, element string) bool {
	for _, v := range slice {
		if v == element {
			return true
		}
	}
	return false
}

func safeHTML(s string) template.HTML {
	return template.HTML(s)
}

func Endpoints() *gin.Engine {
	router := gin.Default()

	router.Static("/static", "./static")
	router.Static("/blogs", "./blogs")

	router.SetFuncMap(template.FuncMap{
		"safe": safeHTML,
	})

	router.LoadHTMLGlob("templates/*")

	router.GET("/", func(c *gin.Context) {
		allMetadata, err := fileops.GetAllBlogMetadata()
		if err != nil {
			if strings.Contains(err.Error(), "no such file or directory") || len(allMetadata) == 0 {
				c.HTML(200, "index.html", gin.H{
					"Blogs": []fileops.BlogMetadata{},
				})
				return
			}
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}

		c.HTML(200, "index.html", gin.H{
			"Blogs":   allMetadata,
			"NoBlogs": len(allMetadata) == 0,
		})
	})

	router.GET("/:blogName", func(c *gin.Context) {
		blogName := c.Param("blogName")
		dirPath := fmt.Sprintf("./blogs/%s", blogName)

		if _, err := os.Stat(dirPath); os.IsNotExist(err) {
			c.HTML(404, "404.html", gin.H{
				"Message": "Oops! The blog you are looking for does not exist.",
			})
			return
		}

		metadata, err := fileops.ReadBlogMetadataYaml(dirPath, blogName)
		if err != nil {
			c.HTML(404, "404.html", gin.H{
				"Message": "Oops! The blog you are looking for does not exist.",
			})
			return
		}

		htmlContent, err := fileops.MarkdownContentToHTML(dirPath)
		if err != nil {
			c.HTML(500, "500.html", gin.H{"error": err.Error()})
			return
		}

		updatedHTMLContent := strings.ReplaceAll(htmlContent, "src=\"images/", fmt.Sprintf("src=\"./blogs/%s/images/", blogName))

		c.HTML(200, "blog.html", gin.H{
			"Title":         metadata.Title,
			"Author":        metadata.Author,
			"Date":          metadata.Date,
			"Content":       updatedHTMLContent,
			"DirectoryName": blogName,
		})
	})

	router.NoRoute(func(c *gin.Context) {
		c.HTML(404, "404.html", gin.H{
			"Message": "Oops! The page you are looking for does not exist.",
		})
	})

	return router
}
