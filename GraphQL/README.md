# Query

```
mutation MyMutation($users: [ID]) {
  __typename
  updateWorkspace(owner: "2", id: "4", users: $users) {
    workspace {
      id
      name
    }
  }
}
```

# Query variables

```
{"users": [1,2,3]}
```

