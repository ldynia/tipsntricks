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
