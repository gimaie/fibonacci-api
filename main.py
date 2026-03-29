from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from fib_calc import fibonacci

app = FastAPI()

@app.exception_handler(Exception)
async def server_exception_handler(request: Request, exc: Exception):
  return JSONResponse(
        status_code=500,
        content={"status": 500, "message": "サーバー内部でエラーが発生しました。"}
  )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
  return JSONResponse(
    status_code=400,
    content={"status": 400, "message": "nには整数を指定してください。"}
  )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
  return JSONResponse(
    status_code=exc.status_code,
    content={"status": exc.status_code, "message": exc.detail}
  )

@app.get("/fib")
def get_fibonacci(n: int):
  if n < 1:
    raise HTTPException(status_code=400, detail="nは1以上の整数を指定してください。")
  if n > 10000:
    raise HTTPException(status_code=400, detail="nは10000以下にしてください。")
  result = fibonacci(n)
  if result == -1:
    raise HTTPException(status_code=400, detail="不正な入力です。")
  return {"result": result}