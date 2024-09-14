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

	router.GET("/:blogName", func(c *gin.Context) {
		blogName := c.Param("blogName")
		dirPath := fmt.Sprintf("./blogs/%s", blogName)

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

		c.JSON(200, gin.H{
			"Title":   metadata.Title,
			"Author":  metadata.Author,
			"Date":    metadata.Date,
			"Content": htmlContent,
		})
	})

	router.GET("/", func(c *gin.Context) {
		allMetadata, err := fileops.GetAllBlogMetadata()
		if err != nil {
			c.JSON(500, gin.H{"error": err.Error()})
			return
		}
		c.JSON(200, allMetadata)
	})
	return router
}
