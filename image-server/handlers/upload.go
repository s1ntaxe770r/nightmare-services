package handlers

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Upload() gin.HandlerFunc {
	return func(c *gin.Context) {
		file, _ := c.FormFile("image")
		c.SaveUploadedFile(file, fmt.Sprintf("./images/%s", file.Filename))
		c.String(http.StatusOK, "image upload successful")
	}
}
