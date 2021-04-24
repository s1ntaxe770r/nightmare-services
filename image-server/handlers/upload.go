package handlers

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
)

var links_server = os.Getenv("LINKS_SERVER")

// Upload handles file uploads
func Upload() gin.HandlerFunc {
	return func(c *gin.Context) {
		file, _ := c.FormFile("image")
		c.SaveUploadedFile(file, fmt.Sprintf("./images/%s", file.Filename))
		updatelinks(file.Filename)
		c.String(http.StatusOK, "image upload successful")
	}
}

func updatelinks(filename string) {
	type Payload struct {
		ImageName string `json:"image_name"`
	}

	data := Payload{
		ImageName: filename,
	}
	payloadBytes, err := json.Marshal(data)
	if err != nil {
		log.Fatal(err)
	}
	body := bytes.NewReader(payloadBytes)

	req, err := http.NewRequest("POST", links_server+"/links/store", body)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

}
