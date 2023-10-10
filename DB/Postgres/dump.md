# Azure

[Azure](https://docs.microsoft.com/en-us/azure/postgresql/howto-migrate-using-dump-and-restore)

```bash
$ pg_dump -Fc -v --port=11044 --username=postgres --dbname=postgres -f postgres.dump
$ createdb -h localhost --port 11044 --username postgres -w postgres
$ pg_restore -v --no-owner --port=11044 --username=postgres --dbname=postgres --clean postgres.dump
```

# Django

```bash
$ python manage.py dumpdata > data.json
$ python manage.py loaddata data.json
```

# Single DB

### SQL

```bash
$ pg_dump -p $POSTGRES_PORT -c -U postgres > dump_`date +%d-%m-%Y`.sql
$ pg_restore -v --no-owner -p $POSTGRES_PORT -U postgres --dbname=postgres --clean dump_04-08-2021.sql
```

### Docker

```bash
$ docker exec -t boilerplate_postgres pg_dump -p 11044 -U postgres > dump_`date +%d-%m-%Y`.sql
$ cat dump_03-08-2021.sql | docker exec -i boilerplate_postgres psql -p 11044 -U postgres -d postgres
```
# ALL DBs

### SQL

```bash
$ pg_dumpall -p $POSTGRES_PORT -c -U postgres > dump_all_`date +%d-%m-%Y`.sql
$ psql -f dump_all_03-08-2021.sql -p $POSTGRES_PORT -d postgres postgres
```
### Docker

```bash
$ docker exec -t boilerplate_postgres pg_dumpall -p 11044 -U postgres > dump_all_`date +%d-%m-%Y`.sql
$ docker exec -i boilerplate_postgres psql -f /dump_all_03-08-2021.sql -p $POSTGRES_PORT -d postgres postgres
$ docker exec -i boilerplate_postgres psql -f /dump_all_03-08-2021.sql -p 11044 -d postgres postgres
```
