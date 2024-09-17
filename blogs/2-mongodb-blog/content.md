### MongoDB: NoSQL Database for Modern Applications

---

![MongoDB](images/mongodb.png)

MongoDB is a document-oriented NoSQL database that provides high performance, high availability, and easy scalability. Instead of storing data in rows and columns, it stores data in flexible, JSON-like documents.

#### Why Choose MongoDB?

- **Schema-less**: No need to define the structure of documents.
- **Horizontal Scalability**: MongoDB scales easily with sharding.
- **Rich Query Language**: Supports ad-hoc queries, indexing, and real-time aggregation.

#### Example: Inserting a Document

```javascript
db.users.insertOne({
  name: "Alice",
  age: 25,
  hobbies: ["reading", "biking", "cooking"]
})
```

This MongoDB query inserts a document into the `users` collection with fields like `name`, `age`, and `hobbies`.

#### Resources to Learn MongoDB
- [MongoDB University](https://university.mongodb.com/)
- [Official Documentation](https://docs.mongodb.com/)
