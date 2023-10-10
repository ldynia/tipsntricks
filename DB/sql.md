
# SQL 

## Custom JOINS
```sql
SELECT * FROM sample WHERE first_file_id='835537cd-1b3d-4c8d-881b-56dbb00d8d09'
SELECT * FROM file_upload WHERE status !='complete'
SELECT * FROM file_upload WHERE filename Like '%DTU2018-35-PRJ1138-staphylococcus-aureus-2008%'
SELECT * FROM file_upload WHERE md5_checksum='ffb54d505373bdfb7b997d88b7536be0' OR md5_checksum='86f364673e1adb49db98ac13eb8d91f9'

SELECT * FROM file_upload
LEFT JOIN file_upload_metadata
ON file_upload.id=file_upload_metadata.file_upload_id
WHERE file_upload.user_id=17

SELECT * FROM file_upload
LEFT JOIN file_upload_metadata
ON file_upload.id=file_upload_metadata.file_upload_id
WHERE file_upload.user_id=17 AND file_upload.filename='S05130-09_R1.fastq.gz'

SELECT file_upload.md5_checksum, COUNT(file_upload.md5_checksum) AS dup_count
FROM file_upload
WHERE file_upload.user_id=17
GROUP BY file_upload.md5_checksum
HAVING COUNT(file_upload.md5_checksum) > 1
ORDER BY file_upload.md5_checksum DESC


SELECT T1.dup_count, T1.md5_checksum, T2.user_id, T2.status
FROM (
  SELECT file_upload.md5_checksum, COUNT(file_upload.md5_checksum) AS dup_count
  FROM file_upload
  WHERE file_upload.user_id=17
  GROUP BY file_upload.md5_checksum
  HAVING COUNT(file_upload.md5_checksum) > 1
  ORDER BY file_upload.md5_checksum DESC
) AS T1
JOIN (
  SELECT * FROM file_upload
) AS T2
ON T1.md5_checksum = T2.md5_checksum


SELECT DISTINCT T1.dup_count, T1.md5_checksum, T2.status
FROM (
  SELECT file_upload.md5_checksum, COUNT(file_upload.md5_checksum) AS dup_count
  FROM file_upload
  GROUP BY file_upload.md5_checksum
  HAVING COUNT(file_upload.md5_checksum) > 1
  ORDER BY file_upload.md5_checksum DESC
) AS T1
JOIN (
  SELECT * FROM file_upload
) AS T2
ON T1.md5_checksum = T2.md5_checksum
```



## Views - SQLite example

```sql
CREATE TABLE "demo" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL
);

CREATE UNIQUE INDEX idx_demo_id ON demo(id);
CREATE INDEX idx_demo_last_name ON demo(last_name);

INSERT INTO demo (first_name, last_name) VALUES ("lukasz", "dynowski");
INSERT INTO demo (first_name, last_name) VALUES ("martin", "andersen");

SELECT * FROM demo;

CREATE VIEW view_demo_full_name AS
SELECT 
    id,
    first_name || ' ' || last_name AS full_name
FROM demo;
  
SELECT * FROM view_demo_full_name;

SELECT demo.id, demo.first_name, demo.last_name, view_demo_full_name.full_name
FROM demo
INNER JOIN view_demo_full_name ON view_demo_full_name.id = demo.id
ORDER BY view_demo_full_name.full_name DESC


INSERT INTO demo (first_name, last_name) VALUES ("darth", "vader");

SELECT * FROM demo;
```

