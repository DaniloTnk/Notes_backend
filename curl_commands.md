# Some commands to test api endpoints.

## Get HealthCheck

curl -X 'GET' 'http://127.0.0.1:8000/api/healthcheck/' -H 'accept: _/_'

## Get list all of notes

curl -X 'GET' 'http://127.0.0.1:8000/api/notes/' -H 'accept: application/json'

## Get a note by id

curl -X 'GET' 'http://127.0.0.1:8000/api/notes/1/' -H 'accept: application/json'

## Create a note

curl -X 'POST' \
 'http://127.0.0.1:8000/api/notes/' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -H 'X-CSRFTOKEN: br3tVL5ygFeBBhAaBYWr8xsoTODSbauJjjfZhFmiZdY7sQvukGqDrkb5GUQWJkVA' \
 -d '{
"title": "Curl Title",
"content": "Curl content created."
}'

## Update a note data change {ID} to a valid note id add CSRFTOKEN

## If you are updating just one field you can use PATCH instead of PUT.

curl -X 'PUT' \
 'http://127.0.0.1:8000/api/notes/{ID}/' \
 -H 'accept: application/json' \
 -H 'Content-Type: application/json' \
 -H 'X-CSRFTOKEN: ' \
 -d '{
"title":"Curl Title EDITED",
"content": "Curl content edited."
}'

## Delete a note you need the csrftoken to delete.

curl -X 'DELETE' \
 'http://127.0.0.1:8000/api/notes/6/' \
 -H 'accept: _/_' \
 -H 'X-CSRFTOKEN: '
