from fastapi import APIRouter, HTTPException, status, Body, Depends, Request
from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from business_rules.Gather_Variable_A import Gather_Variable_A


calculadora_router = APIRouter(
    tags = ["calculadora01"]
)


# http://localhost:8080/calculadora01/?number_A=10&number_B=2
# curl -X GET "http://localhost:8080/calculadora01/?number_A=10&number_B=2"
@calculadora_router.get("/")
async def multiple_two_numbers(number_A:int, number_B:int) -> dict:
    result = number_A * number_B
    return(
            {"message":"multipled result is {0}".format(result),
             "detail":"detalhes"
             }
          )


#curl -X GET "http://localhost:8080/calculadora01/my?number_A=10&number_B=2&number_C=3"
@calculadora_router.get("/my")
async def multiple_two_numbers(number_A:int, number_B:int, number_C:int) -> dict:
    result = number_A * number_B *  number_C
    return(
            {"message":"multipled result is {0}".format(result),
             "detail":"detalhes"
             }
          )



# curl -X GET "http://localhost:8080/calculadora01/sum?number_A=10&number_B=2"
@calculadora_router.get("/sum")
async def sum_two_numbers(number_A:int, number_B:int) -> dict:
    result = number_A + number_B
    return(
            {
             "message":"sum result is {0}".format(result),
             "detail":"detalhes"
             }
          )


# curl -X GET "http://localhost:8080/calculadora01/diff?number_A=10&number_B=2"
@calculadora_router.get("/diff")
async def diff_two_numbers(number_A:int, number_B:int) -> dict:
    result = number_A - number_B
    return(
            {
             "message":"diff result is {0}".format(result),
             "detail":"detalhes"
             }
          )

# curl -X GET "http://localhost:8080/calculadora01/div?number_A=10&number_B=2"
@calculadora_router.get("/div")
async def div_two_numbers(number_A:int, number_B:int) -> dict:
    result = number_A / number_B
    return(
            {
             "message":"diff result is {0}".format(result),
             "detail":"detalhes"
             }
          )


# curl -X GET "http://localhost:8080/calculadora01/mod?number_A=10&number_B=2"
@calculadora_router.get("/mod")
async def mod_two_numbers(number_A:int, number_B:int) -> dict:
    result = number_A % number_B
    return(
            {
             "message":"diff result is {0}".format(result),
             "detail":"detalhes"
             }
          )


# curl -X GET "http://localhost:8080/calculadora01/variable_A?number_A=3"
@calculadora_router.get("/variable_A")
async def get_variable_A(number_A:int) -> dict:

    result = Gather_Variable_A().get_variable_A(number_A)
    return(
            {
             "message":"variable A result is {0}".format(result),
             "detail":"detalhes",
             "delano": "oxy"
             }
          )

# receive parameter inside the body
# curl -X POST "http://localhost:8080/calculadora01/teste_post/" \
# -H 'accept: application/json' \
# -H 'Content-Type: application/json' \
# -d '{
#     "number_A": 1000,
#     "number_B": 2
#     }'"
@calculadora_router.post("/teste_post")
async def get_variable_A(number_A:int = Body(...),
                         number_B:int = Body(...)) -> dict:
    print(number_A)
    print(number_B)
    # result = Gather_Variable_A().get_variable_A(number_A)
    result = number_A * number_B
    return(
            {
             "message":"variable A result is {0}".format(result),
             "detail":"detalhes",
             "delano": "oxy"
             }
          )

# @app.post("/route/")
# def my_route(username: str = Body(...), password: str = Body(...)) -> None:
#     print("username:", username)
#     print("password length:", len(password))