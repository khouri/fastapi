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


-- testing planer app
curl -X 'POST' \
'http://0.0.0.0:8080/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@packt.com",
"password": "Stro0ng!",
"username": "FastPackt"
}'

curl -v -X 'POST' \
'http://0.0.0.0:8080/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@packt.com",
"password": "Stro0ng!"
}'


-- CH 05 planer

curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'




# Sobre MongoDB
Install mongosh:
```shell
brew install mongosh
```

imagem docker do mongoDB:
```shell
docker pull mongodb/mongodb-community-server:latest
```

run the image as a container
```shell
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```


mongosh "mongodb+srv://YOUR_CLUSTER_NAME.YOUR_HASH.mongodb.net/" --apiVersion YOUR_API_VERSION --username YOUR_USERNAME


show databases


mongosh "mongodb://localhost:27017"

show collections
show tables
db.getCollectionNames()


mongo --quiet --eval  "printjson(db.adminCommand('listDatabases'))"


Awsome ressources about sqlalchemy:
https://github.com/dahlia/awesome-sqlalchemy


python generators:
https://www.kdnuggets.com/2023/02/getting-started-python-generators.html#:~:text=Under%20the%20hood%2C%20the%20generator,generator%20function%20suspends%20execution%20temporarily.


https://towardsdatascience.com/cpython-internals-how-do-generators-work-ba1c4405b4bc

https://medium.com/@anuj_shah/creating-custom-data-generator-for-training-deep-learning-models-part-1-5c62b20cff26

https://machinelearningsite.com/python-generators-in-machine-learning/


https://realpython.com/introduction-to-python-generators/


https://www.alura.com.br/artigos/conhecendo-os-geradores-no-python?utm_term=&utm_campaign=%5BSearch%5D+%5BPerformance%5D+-+Dynamic+Search+Ads+-+Artigos+e+Conte%C3%BAdos&utm_source=adwords&utm_medium=ppc&hsa_acc=7964138385&hsa_cam=11384329873&hsa_grp=164240702375&hsa_ad=703853654617&hsa_src=g&hsa_tgt=dsa-2276348409543&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwy8i0BhAkEiwAdFaeGPRD0zNgNAX8jGoromU9jFaLQDaGodY2iD4zxhlc1_BZcXkiQ2xjAxoCvkIQAvD_BwE



curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"title": "FastAPI Book Launch",
"image": "https://linktomyimage.com/image.png",
"description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
"tags": [
"python",
"fastapi",
"book",
"launch"
],
"location": "Google Meet"
}'

curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'

curl -X 'GET' \
'http://0.0.0.0:8080/event/6698657e5a8ea1965e39af83' \
-H 'accept: application/json'


curl -X 'PUT' \
'http://0.0.0.0:8080/event/669861814457690e4bad4ccd' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"location": "Hybrid"}'

curl -X 'DELETE' \
'http://0.0.0.0:8080/event/669861814457690e4bad4ccd' \
-H 'accept: application/json'




curl -X 'POST' \
'http://0.0.0.0:8080/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@packt.com",
"password": "strong!!!",
"events": []
}'


--signin method
curl -X 'POST' \
'http://0.0.0.0:8080/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "fastapi@packt.com",
"password": "strong!!!"
}'



db.users('test').find([])


# how to configure .env:
DATABASE_URL=mongodb://localhost:27017/test


mongosh "mongodb://localhost:27017"
show collections
db.users.find({})


curl -X 'POST' \
'http://0.0.0.0:8080/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "reader@packt.com",
"password": "exemplary"
}'



-- curl to test after the Oauth:
curl -X 'POST' \
'http://0.0.0.0:8080/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=&username=reader%40packt.com&password=exemplary&scope=&client_id=&client_secret='




calculadora:
curl -X GET "http://localhost:8080/calculadora01/?number_A=10&number_B=2"



docker-compose up -d

docker-compose down

curl -X POST "http://localhost:8080/calculadora01/teste_post" \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "number_A": "1000",
    "number_B": "2"
    }'

curl -X 'POST' \
'http://0.0.0.0:8080/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "reader@packt.com",
"password": "exemplary"
}'


curl -X POST "http://localhost:8080/calculadora01/teste_post" \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "number_A": 1000,
    "number_B": 2
    }'


Path and query parameters
In the previous section, we learned what models are and how they are used to validate
request bodies. In this section, you’ll learn what path and query parameters are, the role
they play in routing, and how to use them.

Path parameters
Path parameters are parameters included in an API route to identify resources. These
parameters serve as an identifier and, sometimes, a bridge to enable further operations in
a web application.
We currently have routes for adding a todo and retrieving all the todos in our todo
application. Let’s create a new route for retrieving a single todo by appending the todo’s ID
as a path parameter.




