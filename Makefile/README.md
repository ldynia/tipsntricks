```Makfile
# This Makefile is a template encapsulating the common behavior of our applicationapp.
# If you have application specific use case that you would like to add.
# Then, please craete Makefile downstream the project and iclude reference to this file.

.DEFAULT_GOAL = default_help

# Extract args for docs, seed, unit_test target
TARGETS=docs,seed,unit_test
ifneq ($(findstring $(firstword $(MAKECMDGOALS)),$(TARGETS)),)
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(ARGS):;@:)
endif

build:
	@echo "Building/Rebuilding the application"
	docker-compose --file $$PWD/.devcontainer/docker-compose.yml build --no-cache

clean:
	@echo "Wiping application and application's artifacts"
	docker-compose --file .devcontainer/docker-compose.yml down

	docker volume ls | grep ${CONTAINER} | awk '{print $$2}' | xargs docker volume rm

	docker image ls | grep ${PROJECT} | awk '{print $$1}' | xargs docker image rm
	docker image prune --force

coverage:
	@echo "Run code coverage"
	docker exec ${BACKEND_CONTAINER} /app/scripts/test.sh

docs:
	@echo "Generateing application document artifacts"
ifndef ARGS
	@echo "Please provide application(s) name!";
else
	docker exec ${BACKEND_CONTAINER} python manage.py graph_models -X *_Abstract -g -o UML.png $(ARGS)
endif

start:
	@echo "Starting application"
	docker-compose --file $$PWD/.devcontainer/docker-compose.yml up --detach

stop:
	@echo "Stopping application"
	docker-compose --file $$PWD/.devcontainer/docker-compose.yml stop

unit_test:
	@echo "Run unit tests"
	docker exec ${BACKEND_CONTAINER} python manage.py test -v 2 $(ARGS)

default_help:
	@echo  "build		- Build/Rebuild the application."
	@echo  "clean		- Wipe application and application's artifacts."
	@echo  "coverage	- Run code coverage."
	@echo  "docs		- Generate application document artifacts."
	@echo  "help		- Print help."
	@echo  "start		- Start application."
	@echo  "stop		- Stop application."
	@echo  "unit_test	- Run unit tests."
```

```Makfile
SHELL = /bin/sh
PROJECT = delphi
CONTAINER = devcontainer
BACKEND_CONTAINER = ${PROJECT}_backend

include ./backend/general/Makefile

.DEFAULT_GOAL = help

seed:
	@echo "Populating database with dummy data!!!!!!";
ifndef ARGS
	@echo "Please provide leo email!";
else
	@echo "Import public datasets"
	docker exec ${BACKEND_CONTAINER} python manage.py import_chemprop;

	@echo "Sync Chemprop"
	docker exec ${BACKEND_CONTAINER} python manage.py sync_chemprop;

	@echo "Create dummy ChemProp model (with valid user email to select workspaces)"
	docker exec ${BACKEND_CONTAINER} python manage.py dummy_chemprop $(ARGS);
endif

help: default_help
	@echo  "seed		- Populate application with data."
```
