# Simple Proxy in Go

## Working

- The working of it is simple as it the request is being hit to server it intercepts the requests clones it and makes a new request.
- It clones the response as well and serves back. Feel free to add custom headers, and things.
- This only works for `http` websites.

```bash
curl -x "http://localhost:8081" "http://www.example.com"
```
