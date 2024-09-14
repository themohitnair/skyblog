# Building Web Applications with Go Gin Framework

![Go Gin Logo](images/go-gin-logo.png)

Gin is a web framework written in Go (Golang). It features a martini-like API with much better performance, up to 40 times faster. If you need performance and good productivity, you will love Gin.

## Key Features of Gin

1. **Fast**: Radix tree based routing, small memory foot print. No reflection. Predictable API performance.
2. **Middleware support**: An incoming HTTP request can be handled by a chain of middlewares and the final action.
3. **Crash-free**: Gin can catch a panic occurred during a HTTP request and recover it.
4. **JSON validation**: Gin can parse and validate the JSON of a request - for example, checking the existence of required values.
5. **Routes grouping**: Organize your routes better. Authorization required vs non required, different API versions...
6. **Error management**: Gin provides a convenient way to collect all the errors occurred during a HTTP request.
7. **Built-in rendering**: Gin provides an easy to use API for JSON, XML and HTML rendering.

## Quick Start

Here's a simple example of a Gin application:

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })
    r.Run() // listen and serve on 0.0.0.0:8080
}
```

To run this application, save it as `main.go` and execute:

```
go run main.go
```

Visit `http://localhost:8080/ping` to see the JSON response.

## Handling Parameters

Gin makes it easy to handle various types of parameters:

```go
func main() {
    router := gin.Default()

    // This handler will match /user/john but will not match /user/ or /user
    router.GET("/user/:name", func(c *gin.Context) {
        name := c.Param("name")
        c.String(http.StatusOK, "Hello %s", name)
    })

    // However, this one will match /user/john/ and also /user/john/send
    router.GET("/user/:name/*action", func(c *gin.Context) {
        name := c.Param("name")
        action := c.Param("action")
        message := name + " is " + action
        c.String(http.StatusOK, message)
    })

    router.Run(":8080")
}
```

## Conclusion

Gin provides a robust toolkit for building web applications and APIs with Go. Its speed, flexibility, and feature set make it an excellent choice for developers looking to create high-performance web services.