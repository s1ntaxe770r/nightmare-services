package main

import (
	"image-server/handlers"
	"net/http"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.Use(cors.Default())
	router.LoadHTMLGlob("templates/*")
	router.StaticFS("/images", http.Dir("./images"))
	router.GET("/", handlers.Index())
	router.POST("/upload", handlers.Upload())
	router.Run(":8000")
}
