from fastapi import FastAPI
from fa_learn_app.routers import student
from fa_learn_app.routers import group


def set_routers(app: FastAPI):
    app.include_router(student.router, prefix="", tags=[])
    app.include_router(group.router, prefix="", tags=[])
