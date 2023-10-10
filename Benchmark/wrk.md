- https://github.com/wg/wrk
- https://github.com/giltene/wrk2

- https://nitikagarw.medium.com/getting-started-with-wrk-and-wrk2-benchmarking-6e3cdc76555f
- https://medium.com/@felipedutratine/intelligent-benchmark-with-wrk-163986c1587f

**post.lua**
```
wrk.method = 'POST'
wrk.body = '{"input":[1,2,3,4]}'
wrk.headers['Content-Type'] = 'application/json'
wrk.headers['Cookie'] = 'fesfsefesfesf'
```

```bash
wrk -c2 -t2 -d10s -s post.lua --latency https://some.example.com/endpoint
```
