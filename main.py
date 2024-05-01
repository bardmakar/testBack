from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title = 'Super Quiz App'
)

@app.post('/check')
async def check(text: str):
    ...

# class Quiz(BaseModel):
#     id: int
#     answers: Dict[str, int]

# quiz1 = [1, 4, 3, 2]

# @app.post('/check_quiz')
# def check_quiz(quiz: Quiz):
#     correct = 0
#     for question, answer in quiz.answers.items():
#         if answer == quiz1[int(question) - 1]:
#             correct += 1
#     percent = (correct * 100) / len(quiz.answers)
#     if percent > 100 or percent < 0:
#         return {'ok': False, 'msg': 'Percent error'}
#     else:
#         if percent >= 90:
#             grade = 'H'
#         if 70 <= percent < 90:
#             grade = 'Q'
#         if 50 <= percent < 70:
#             grade = 'S'
#         if percent < 50:
#             grade = 'L'
#         return {'ok': True, 'grade': grade, 'percent': percent}