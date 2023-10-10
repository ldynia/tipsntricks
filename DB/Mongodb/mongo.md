# MongoDB

### Links
* [Data Modeling Introduction](https://docs.mongodb.com/manual/core/data-modeling-introduction/)
* [Schema Validation](https://docs.mongodb.com/manual/core/schema-validation/)
* [Data Models Relationships](https://docs.mongodb.com/manual/applications/data-models-relationships/)

### Basic Interaction
```bash
$ mongo
> show dbs
> use webshop

# insert
> db.posts.insertOne({title: "hello", content: "Hello Mongo!"})

# find
> db.posts.find().pretty()
> db.posts.find({title: {$eq: "hello"}}, {content:1})
> db.posts.findOne().preaty()
```

#### Backup and mongorestore
```bash
mongoexport --db phenex_dev --collection backend_users --out db.json
mongoimport --db phenex_dev --collection backend_users db.json

mongodump --db phenex_dev --out /data/db/backup/fixtures
mongorestore /data/db/backup/fixtures

mongodump --db phenex_dev --out backup/db_`date +"%m-%d-%y"`
# mongodump --gzip --db phenex_dev --out backup`date +"%m-%d-%y"`.backup
mongodump --gzip --db phenex_dev --out db.backup
mongorestore db.backup --gzip
```
