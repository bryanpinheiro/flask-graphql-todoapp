# GraphQL API Operations

## Queries

### Get All Todos

```graphql
query GetAllTodos {
  todos {
    id
    title
    completed
  }
}
```

### Get Todo By ID

```graphql
query GetTodoById($todoId: Int!) {
  todo(todoId: $todoId) {
    id
    title
    completed
  }
}
```

## Mutations

### Create Todo

```graphql
mutation CreateTodo($title: String!) {
  createTodo(todoInput: { title: $title }) {
    todo {
      id
      title
      completed
    }
  }
}
```

- query variable
```graphql
{
  "title": "Bryan"
}
```

### Update Todo

```graphql
mutation UpdateTodo($todoId: Int!, $data: TodoInput!) {
  updateTodo(todoId: $todoId, data: $data) {
    todo {
      id
      title
      completed
    }
  }
}
```

### Delete Todo

```graphql
mutation DeleteTodo($todoId: Int!) {
  deleteTodo(todoId: $todoId)
}
```


In this example:

- Each operation (query or mutation) is under a corresponding heading.
- The GraphQL code is wrapped in fenced code blocks (triple backticks) with the language specified as `graphql` for syntax highlighting.
- For queries with variables, the variables are specified in the GraphQL operation with placeholders (e.g., `$todoId`).
- Replace `$todoId` and `$title` with actual values when using the queries or mutations.
