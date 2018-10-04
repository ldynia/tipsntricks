# Testing

[Benchmarking](https://www.digitalocean.com/community/tutorials/how-to-benchmark-http-latency-with-wrk-on-ubuntu-14-04)


### Requests Test
```
$ wrk -t2 -c5 -d5s --timeout 2s http://compare.dev/
$ wrk -t2 -c5 -d5s --timeout 2s http://compare.dev/app/api/v1/newsfeed
```
