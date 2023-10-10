# Snyk

```bash
# Mount project file system into container
$ docker run --rm -d -v $PWD:/app --name cve_scanner python:3.7 sleep infinity
$ docker exec cve_scanner sh -c "apt-get update; apt-get install -y nodejs npm"

# Scan npm project
$ docker exec cve_scanner npm install -g snyk
$ docker exec cve_scanner npm install /app/frontend
$ docker exec cve_scanner pip install -r /app/backend/general/requirements.txt -r /app/backend/requirements.txt

# Scan backend project
$ docker exec cve_scanner snyk test --file=/app/backend/requirements.txt --command=python3
$ docker exec cve_scanner snyk test --file=/app/backend/general/requirements.txt --command=python3

# Scan image project
$ snyk container test delphi_backend
```
