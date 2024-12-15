from fastapi import FastAPI, Path
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: int = Path(ge=1, lt=100, description="Enter User ID", example="1")):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get('/user/{username}/{age}')
async def info(username: str = Path(min_length=5, max_length=20, description="Enter username", example="Enter age"), age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)