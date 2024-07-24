from fastapi import FastAPI
# from routes.users import user_router
# from routes.events import event_router
from routes.calculadora01 import calculadora_router
import uvicorn

# from database.connection import Settings
# from fastapi.middleware.cors import CORSMiddleware


# settings = Settings()

app = FastAPI()
app.include_router(calculadora_router, prefix="/calculadora01")
# app.include_router(event_router, prefix="/event")

# origins = ["*"]
# app.add_middleware(
#                     CORSMiddleware,
#                     allow_origins=origins,
#                     allow_credentials=True,
#                     allow_methods=["*"],
#                     allow_headers=["*"],
#                 )

# @app.on_event("startup")
# async def init_db():
#     await settings.initialize_database()


if __name__ == '__main__':
    uvicorn.run("main:app", host = "0.0.0.0", port = 8080, reload=True)