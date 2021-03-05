from src.generator import add_problem
import random
from typing import Optional
from fastapi import FastAPI, Request


app = FastAPI()

question = add_problem(1)
operators = {
    "Addition": "+",
    "Subtraction": "-",
    "Multiplication": "*",
    "Division": "/",
}

@app.get("/")
def happy_func():
    return "Happy!"

@app.get("/{arithmatic}")
def read_root(arithmatic: str):
    if arithmatic == "Random":
        return question.create_random_problem()
    elif arithmatic == "Operator":
        sign = "Operator"
        return question.create_arithmatic_problem(sign)
    else:
        sign = operators.get(arithmatic)
        return question.create_arithmatic_problem(sign)
