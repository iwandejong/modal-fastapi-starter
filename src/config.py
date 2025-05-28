import modal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

image = modal.Image.debian_slim().pip_install("fastapi[standard]")

app = modal.App(
  name="modal-fastapi-starter",
  image=image
)

# FastAPI app
web_app = FastAPI()
auth_scheme = HTTPBearer()

web_app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)