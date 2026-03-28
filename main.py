from fastapi import FastAPI
from fib_calc import fibonacci

# FastAPIの本体（アプリケーション）を作成して、appという変数に入れる
app = FastAPI()

# 「/fib」というURLにGETリクエスト（通常のアクセス）が来た時のルール
@app.get("/fib")
def dummy_api(n: int):
    # 受け取った数字「n」を、そのままJSON形式の辞書で返す
    return {
        "message": "Web APIが動きました！",
        "受け取った数字": fibonacci(n)
    }