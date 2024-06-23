package main

import (
	// "fmt"
	"io"
	"log"
	"net/http"
	// "net/url"
)


var customTransport = http.DefaultTransport

func init() {
	// Set timeouts and other rules
}

func handleRequest(w http.ResponseWriter, r *http.Request) {
	// Create a new HTTP request with same method, URL, and body
	targetUrl := r.URL
	log.Println("Received request for: ", targetUrl.String())
	proxyReq, err := http.NewRequest(r.Method, targetUrl.String(), r.Body)
	if err!= nil {
        http.Error(w, "Error creating proxy request", http.StatusInternalServerError)
        return
    }

	// Copy the headers from the original request to the proxy request
	for name, values := range r.Header {
		for _, value := range values {
			proxyReq.Header.Add(name, value);
		}
	}

	// Send the proxy request using the custom transport
	resp, err := customTransport.RoundTrip(proxyReq)
	if err != nil {
		http.Error(w, "Error sending proxy request", http.StatusInternalServerError)
		return
	}
	defer resp.Body.Close();

	// Copy the headers from the proxy response to the original response
	for name, values := range resp.Header {
		for _, value := range values {
			w.Header().Add(name, value)
		}
	}

	// Set the status code of the original response to the status code of proxy response
	log.Println("Received response status code: ", resp.StatusCode)
	w.WriteHeader(resp.StatusCode)

	// Copy the body of proxy response to original rsponse
	io.Copy(w, resp.Body)
}


func main() {
	// Create a new HTTP server with the handleRequest function
	server := http.Server {
		Addr: ":8081",
		Handler: http.HandlerFunc(handleRequest),
	}

	log.Println("Start proxy server on :8081")
	err := server.ListenAndServe()
	if err != nil {
		log.Fatal("Error starting proxy server: ", err)
	}
}
