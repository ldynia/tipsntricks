# Docker

### Docker info
```bash
$ docker info
```

### Add user to docker group
```bash
$ sudo usermod -aG docker <username>
```

### Remove exited containers

```bash
$ sudo docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs sudo docker rm
```
### bash_aliases
```
docker rmi -f $(docker images | grep none | awk '{ print $3 }')
alias drn="docker rmi -f $(docker images | grep none | awk '{ print $3 }')"
```

### Build
```
$ docker build --force-rm -t test .
$ docker build -t cbs/compare:webapp  docker/development

$ docker build  --build-arg BUILD_DATE=$(date -u +'%d-%m-%YT%H:%M:%S') --build-arg GIT_COMMIT=0 --build-arg DEPLOYMENT_ENGINE=uwsgi --build-arg BUILD_BY=lukas --build-arg DEBUG=true -t ldynia/phenex-api:prod -f docker/Dockerfile.production .


```

### Run image / container
```
# run image
$ docker run -it cbs/compare:webapp bash
$ docker run -it -v /home/ludd/Coding/docker/compare:/var/www/compare/ backend

# run container
$ docker exec -it <mycontainer> bash
```

# Remove containers or images
```bash
$ docker rm $(docker ps -a | cut -d ' ' -f1)
$ docker rmi $(docker images | grep none | awk '{print $3}')
```

### Login
```bash
$ docker logs -f compare_webapp_run_3
```

# DOCKER COMPOSE
```bash
$ docker-compose rm --all

$ docker-compose -f docker-compose-production.yml up -d
$ docker-compose -f docker-compose-development.yml up --build
$ docker-compose -f docker-compose-production.yml -p compare_development up

$ docker-compose -f docker-compose-development.yml run webapp
$ docker-compose -f docker-compose-development.yml run -d webapp
```

# Docker Stack

### Manager node
```
$ docker node ls
```

### Create network
```
$ docker network create -d overlay app-net
```

### Create service
```
$ docker service create \
  --name app \
  --publish target=80,published=80 \
  --replicas=5 \
  --network app-net \
  ldynia/hello-flask
```

### Check service
```
$ docker service ls
$ docker service ps app
```


### Deploy service with stacks
```
# app1
$ docker stack deploy -c docker-stack-app.yml app
$ docker service ls
$ docker service rm app_app

# app2
$ docker stack deploy -c docker-stack-app2.yml app
$ docker service ls
$ docker service rm app_frontend app_api
```
