from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn


user_router = APIRouter(
    tags = ["User"]
)

users_lst = {}


@user_router.post("/signup")
async def sign_new_user(data:User) -> dict:
    if data.email in users_lst:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users_lst[data.email] = data
    return(
            {"message": "User sucessfully registered"}
          )

@user_router.post("/signin")
async def sign_user_in(user_data: UserSignIn) -> dict:
    print("first if")
    if user_data.email not in users_lst:
    # if users_lst[user_data.email] not in users_lst:
        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found in DB"
                            )

    print("second if")
    if users_lst[user_data.email].password != user_data.password:
        raise HTTPException(
                                status_code=status.HTTP_403_FORBIDDEN,
                                detail="Wrong credentials"
                            )
    print("before return")
    return(
            {"message":"User sucessfully signed in"}
        )