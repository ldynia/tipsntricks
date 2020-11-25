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

{"users": [1,2,3]}
```

```
mutation MyMutation($workspaceId: ID!, $usersId: [ID]!, $permission: permission!) {
  __typename
  createWorkspacePermission(workspaceId: $workspaceId, usersId: $usersId, permission: $permission) {
    ok
  }
}

{"workspaceId": 24, "usersId": [1,2], "permission": "READ"}
```

