package main

import "sync"
import "net/http"
import "fmt"
import "io"
import "encoding/json"
import "time"

type Item struct {
    Id int `json:"id"`
    Name string `json:"name"`
    Description string `json:"description"`
}

func makeRequest(wg *sync.WaitGroup, mu *sync.Mutex, sucCount *int, failCount *int) {
    defer wg.Done()
    resp, err := http.Get("http://localhost:8081/items")
    mu.Lock()
    defer mu.Unlock()

    if err != nil {
        *failCount++
        return
    }

    defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
    if err != nil {
        *failCount++
    }

    var items []Item

    err = json.Unmarshal(body, &items)

    if err != nil {
        *failCount++
        panic(err)
    }


    *sucCount++
}

func main() {
    var wg sync.WaitGroup
    var mu sync.Mutex

    totalRequests := 150
    var succCount, failCount int

    for t:=0; t < 100; t++ {
        for i := 0; i<totalRequests; i++ {
            wg.Add(1)
            go makeRequest(&wg, &mu, &succCount, &failCount)
        }
        fmt.Printf("bach: %d ", t)
        fmt.Printf("succ: %d, fail: %d\n", succCount, failCount)
        time.Sleep(2*time.Second)
    }

    wg.Wait()

    fmt.Printf("succ: %d, fail: %d\n", succCount, failCount)
}
