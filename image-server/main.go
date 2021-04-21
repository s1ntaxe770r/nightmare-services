package main

import (
	"image-server/handlers"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.StaticFS("/images", http.Dir("./images"))
	router.POST("/upload", handlers.Upload())

	router.Run(":8000")
}
