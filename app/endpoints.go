package app

import (
	"fmt"
	"html/template"
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

func safeHTML(s string) template.HTML {
	return template.HTML(s)
}

func Endpoints() *gin.Engine {
	router := gin.Default()

	router.Static("/static", "./static")

	router.SetFuncMap(template.FuncMap{
		"safe": safeHTML,
	})

	router.LoadHTMLGlob("templates/*")

	router.GET("/:blogName", func(c *gin.Context) {
		blogName := c.Param("blogName")
		dirPath := fmt.Sprintf("./blogs/%s", blogName)
		router.Static("/images", fmt.Sprintf("./blogs/%s/images", blogName))
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

		c.HTML(200, "index.html", gin.H{
			"Blogs": allMetadata,
		})
	})
	return router
}
