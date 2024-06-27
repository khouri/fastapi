# FastAPI Tutorial
https://fastapi.tiangolo.com/tutorial/first-steps/

How to run the simplest file:
fastapi dev main.py


# steps to create a fastapi
Import FastAPI.
Create an app instance.
Write a path operation decorator using decorators like @app.get("/").
Define a path operation function; for example, def root(): ....
Run the development server using the command fastapi dev.
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
https://github.com/OAI/OpenAPI-Specification


## tobe readen
https://fastapi.tiangolo.com/async/#in-a-hurry
https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-13-docker-deploy/
https://learning.christophergs.com/l/ioozh
https://json-schema.org/
https://docs.pydantic.dev/1.10/

https://viniciusarz.medium.com/python-poetry-simplified-a-step-by-step-guide-for-data-scientists-a43716f26c1b
https://realpython.com/dependency-management-python-poetry/
https://medium.com/@sjalexandre/python-tutorial-managing-projects-with-poetry-cd2deab72697


# start the server uvicorn
uvicorn main:app --port 8000 --reload


# send get with curl
curl http://127.0.0.1:8000

curl -X 'GET' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json'


curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "item": "First Todo is to finish this book!"
}'

POST empty body

curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "item": "Validation models help with input types"
}'

curl -X 'GET' \
  'http://127.0.0.1:8000/todo/200' \
  -H 'accept: application/json'


http://127.0.0.1:8000/redoc

http://127.0.0.1:8000/docs


teste da chave rsa
curl -X 'PUT' \
  'http://127.0.0.1:8000/todo/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "item": "Read the next chapter of the book."
}'

curl -X 'DELETE' \
  'http://127.0.0.1:8000/todo/1' \
  -H 'accept: application/json'



curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "item": "Validation models help with input types"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "item": "This todo will be retrieved without exposing my ID!" 
}'