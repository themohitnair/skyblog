package app

import (
	"fmt"
	"skyblog/fileops"

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

func Endpoints() *gin.Engine {
	router := gin.Default()

	router.GET("/", func(c *gin.Context) {

	})

	router.GET("/blog/:id", func(c *gin.Context) {
		blogID := c.Param("id")
		dirPath := fmt.Sprintf("./blogs/%s", blogID)

		metadata, err := fileops.ReadBlogMetadataYaml(dirPath)
		if err != nil {
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}

		htmlContent, err := fileops.MarkdownContentToHTML(dirPath)
		if err != nil {
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}

		c.HTML(200, "blog.html", gin.H{
			"Title":   metadata.Title,
			"Author":  metadata.Author,
			"Date":    metadata.Date.Format("January 2, 2006 15:04 MST"),
			"Content": htmlContent,
		})
	})

	router.GET("/blogs/metadata", func(c *gin.Context) {
		allMetadata, err := fileops.GetAllBlogMetadata()
		if err != nil {
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}

		c.JSON(200, allMetadata)
	})

	return router
}
