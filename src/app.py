import os
import modal
from fastapi import Request, Depends
from fastapi.security import HTTPAuthorizationCredentials
from src.config import web_app, auth_scheme, image, app

from src.model import Model

model = Model()

@web_app.get("/")
async def root() -> dict:
  prediction = model.predict()
  return {
    "message": "Welcome to the FastAPI app!",
    "prediction": prediction
  }

@web_app.post("/endpoint")
async def endpoint(request: Request, token: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> dict:
  # Check if the token matches the expected value
  if token.credentials != os.getenv("AUTH_TOKEN"):
    return {"error": "Unauthorized"}, 401

  return {"message": "This is a protected endpoint"}

@app.function(image=image, secrets=[modal.Secret.from_name("auth-token")])
@modal.asgi_app()
def fastapi_app():
  return web_app