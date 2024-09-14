package main

import (
	"fmt"
	"log"
	"skyblog/app"
)

func main() {
	PORT := 8000
	router := app.Endpoints()

	if err := router.Run(fmt.Sprintf(":%v", PORT)); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
