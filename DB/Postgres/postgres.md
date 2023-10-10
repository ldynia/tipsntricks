# Postgres


Database location **/var/lib/postgresql/data**


### Calculate total uploaded files
```
SELECT SUM("offset")/(1024*1024*1024) FROM "file_upload";
```


### Join file with metadata
```
SELECT * FROM "file_upload_metadata"
INNER JOIN "file_upload"
ON file_upload_metadata.file_upload_id=file_upload.id;

SELECT
  file_upload.id,
  file_upload_metadata.file_upload_id,
  file_upload.user_id,
  file_upload.filename,
  file_upload_metadata.id,
  file_upload_metadata.sample_name,
  file_upload_metadata.ena_accession_nr,
  file_upload_metadata.pre_assembled,
  file_upload_metadata.sequencing_platform,
  file_upload_metadata.sequencing_type,
  file_upload_metadata.isolation_source,
  file_upload_metadata.source_notes,
  file_upload_metadata.pathogenic,
  file_upload_metadata.pathogenicity_notes,
  file_upload_metadata.organism,
  file_upload_metadata.strain,
  file_upload_metadata.subtype,
  file_upload_metadata.collection_date,
  file_upload_metadata.collected_by,
  file_upload_metadata.country,
  file_upload_metadata.region,
  file_upload_metadata.city,
  file_upload_metadata.zip_code,
  file_upload_metadata.latitude,
  file_upload_metadata.longitude,
  file_upload_metadata.location_notes,
  file_upload_metadata.notes,
  file_upload_metadata.created_on
FROM "file_upload_metadata"
INNER JOIN "file_upload"
ON file_upload_metadata.file_upload_id=file_upload.id;

```
### Replace
```
SELECT REPLACE(file, 'data/', 'data/uploads/')
FROM file_upload
UPDATE file_upload SET file = REPLACE(file, 'data/', 'data/uploads/')
```

### FIX Incremented indexes after database import
Python script for fixing keys after db import

http://stackoverflow.com/questions/13670235/after-importing-data-in-postgresql-duplicate-key-value-violates-unique-constrai

```
# database
WITH mx AS (SELECT MAX(id) AS id FROM auth_user)
SELECT setval('auth_user_id_seq', mx.id) AS curseq FROM mx;


# django
from django.contrib.auth.models import User
for i in range(1,10):
    User(email='p407650@mvrht.com',password='123123', username='ziom').save()
    User.objects.get(email='p407650@mvrht.com').delete()
```

### Backup and Restore - develop db
```
# Backup
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/all.db.bak"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/$(date +%s)_all.db.bak"

su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump compare_development > /var/lib/postgresql/data/backup/compare_development.db.bak.sql"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Ft compare_development > /var/lib/postgresql/data/backup/compare_development.db.bak.tar"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare_development > /var/lib/postgresql/data/backup/compare_development.db.bak.comp"

su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump compare_development > /var/lib/postgresql/data/backup/$(date +%s)_compare_development.db.bak.sql"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Ft compare_development > /var/lib/postgresql/data/backup/$(date +%s)_compare_development.db.bak.tar"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare_development > /var/lib/postgresql/data/backup/$(date +%s)_compare_development.db.bak.comp"

# Docekr
docker exec compare_dev_postgres su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/$(date +%s)_all.db.bak.comp"
docker exec compare_dev_postgres su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare_development > /var/lib/postgresql/data/backup/$(date +%s)_compare_development.db.bak.comp"

# Restore
>>> su - postgres -c "psql -f /srv/www/compare/htdocs/db/backup/1504304522.all.db.bak"
>>> su - postgres -c "psql -f /var/lib/postgresql/data/backup/1504304522.all.db.bak compare_development"

su - postgres -c "psql -f /var/lib/postgresql/data/backup/all.db.bak compare_development"
su - postgres -c "psql -U postgres -d compare_development -f /var/lib/postgresql/data/backup/compare_development.db.bak.sql"
su - postgres -c "pg_restore -d compare_development -Ft /var/lib/postgresql/data/backup/compare_development.db.bak.tar"
su - postgres -c "pg_restore -d compare_development -Fc /var/lib/postgresql/data/backup/compare_development.db.bak.comp"

/srv/www/compare/htdocs/storage/permastore/backup/all.db.bak
/srv/www/compare/htdocs/storage/permastore/backup/compare.db.bak.comp

su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /srv/www/compare/htdocs/storage/backup/all.db.bak"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare_development > /srv/www/compare/htdocs/storage/backup/db.compare_development.compressed.bak"

su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall -h database > /srv/www/compare/htdocs/storage/permastore/postgres/backup/all.db.bak"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare_development > /srv/www/compare/htdocs/storage/permastore/postgres/backup/db.compare_development.compressed.bak"

su - postgres -c "psql -f /srv/www/compare/htdocs/storage/backup/all.db.bak"
su - postgres -c "pg_restore -d compare_development -Fc /srv/www/compare/htdocs/storage/backup/compare.db.bak.comp"
```

```
# Backup and Restore - live db

# Backup
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/all.db.bak"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/$(date +%s)_all.db.bak"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare > /var/lib/postgresql/data/backup/compare.db.bak.comp"
su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare > /var/lib/postgresql/data/backup/$(date +%s)_compare.db.bak.comp"

# Docekr
docker exec compare_postgres su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dumpall > /var/lib/postgresql/data/backup/$(date +%s)_all.db.bak.comp"
docker exec compare_postgres su - postgres -c "mkdir -p /var/lib/postgresql/data/backup/ && pg_dump -Fc compare > /var/lib/postgresql/data/backup/$(date +%s)_compare.db.bak.comp"

# Restore
su - postgres -c "psql -f /var/lib/postgresql/data/backup/all.db.bak compare"
su - postgres -c "pg_restore -d compare -Fc /var/lib/postgresql/data/backup/compare.db.bak.comp"
```


### Loggin
http://opyate.com/2015/06/17/add-logging-to-postgresql-on-docker.html
http://stackoverflow.com/questions/722221/how-to-log-postgresql-queries

```
psql -U postgres
psql -d compare -U developer -W

\list
\dt

SELECT * FROM pg_user; DROP USER master;
```

**scripts/startup_postgres.sh**
```

#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" <<-EOSQL
    CREATE USER "$POSTGRES_USER" WITH SUPERUSER PASSWORD '$POSTGRES_PASSWORD';
    CREATE DATABASE "$POSTGRES_DB";
    GRANT ALL PRIVILEGES ON DATABASE "$POSTGRES_DB" TO "$POSTGRES_USER";
EOSQL
```

### DUMP
```
pg_dump -U postgres -a > /var/lib/postgresql/data/backup.data
pg_dump -U postgres -a --format=c > /var/lib/postgresql/data/backup.data
```

### Load
```
psql -U postgres database_name < /var/lib/postgresql/data/backup.data
psql -U postgres database_name < /var/lib/postgresql/data/db.data.bak
```
