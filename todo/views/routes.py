@baseUrl = http://localhost:6400

### Health
GET {{baseUrl}}/api/v1/health

### List All Todos
GET {{baseUrl}}/api/v1/todos

### Get a specific Todo
GET {{baseUrl}}/api/v1/todos/1

### Create a Todo
POST {{baseUrl}}/api/v1/todos
Content-Type: application/json

{
    "title": "An example Todo",
    "description": "This is an example todo",
}

### Update a Todo
PUT {{baseUrl}}/api/v1/todos/1
Content-Type: application/json

{
    "title": "updated title",
}

### Delete a Todo
DELETE {{baseUrl}}/api/v1/todos/1