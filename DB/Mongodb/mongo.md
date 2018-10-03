# MongoDB

### Links
https://docs.mongodb.com/manual/core/data-modeling-introduction/
https://docs.mongodb.com/manual/core/schema-validation/
https://docs.mongodb.com/manual/applications/data-models-relationships/



### Basic Interaction
```bash
$ mongo
> show dbs
> use webshop
> db.posts.insertOne({title: "hello", content: "Hello Mongo!"})
> db.posts.find().pretty()
> db.posts.find({title: {$eq: "hello"}}, {content:1})
> db.posts.findOne().preaty()
```
