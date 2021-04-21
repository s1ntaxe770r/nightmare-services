package main

import (
	"image-server/handlers"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.POST("/upload", handlers.Upload())

	router.Run(":8000")
}
