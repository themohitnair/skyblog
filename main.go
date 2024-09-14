package main

import (
	"log"
	"skyblog/app"
)

func main() {
	router := app.Endpoints()

	if err := router.Run(":8080"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
