FROM golang:latest as builder

RUN mkdir /app

WORKDIR /app

COPY go.mod .

COPY go.sum .

RUN go mod download 

COPY . . 

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o server

FROM alpine 

RUN apk add --no-cache ca-certificates

COPY --from=builder /app/server /app/server 

RUN mkdir -p /app/images

EXPOSE 8000

ENTRYPOINT ["/app/server"]


