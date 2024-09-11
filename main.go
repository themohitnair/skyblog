package main

import (
	"fmt"
	"skyblog/app"
)

const PORT = 8000

func main() {
	router := app.SetupRouter()
	router.Run(fmt.Sprintf(":%v", PORT))
}
