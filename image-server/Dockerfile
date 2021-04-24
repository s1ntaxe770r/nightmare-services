FROM golang:latest as builder

WORKDIR /app

COPY go.mod .

COPY go.sum .

RUN go mod download 

COPY . . 

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

FROM alpine 

RUN apk add --no-cache ca-certificates

COPY --from=builder /app/image-server /image-server 


EXPOSE 8000

ENTRYPOINT ["/app/image-server"]
