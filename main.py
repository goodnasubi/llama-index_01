# Copyright (c) 2024 Your Name or Organization

from fastapi import FastAPI

from logger_setup import logger
from reader.web import create_index

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello from FastAPI (llama-index-01)!"}


if __name__ == "__main__":
    index = create_index()
    # クエリエンジン作成
    query_engine = index.as_query_engine()
    q = "Exiis Labについて教えて"
    response = query_engine.query(q)
    logger.info(f"クエリ: {q}")
    logger.info(f"クエリ実行結果: {response}")
