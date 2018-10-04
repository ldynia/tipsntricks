# Nginx


```bash
$ setsebool -P httpd_can_network_connect 1
```

```
# Reverse Proxy /etc/nginx/conf.d/app.conf
upstream some-app {
  server node2:5000;
}

server {
  listen       80;
  server_name  app.cnode.local;

  error_log  /var/log/nginx/error.log;
  access_log  /var/log/nginx/access.log;

  location / {
    proxy_set_header HOST $host;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_pass $scheme://some-app/;
  }
}
```
