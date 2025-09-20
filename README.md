# llama-index_01

## 起動方法（FastAPI + gunicorn + uvicorn worker）

1. 必要なパッケージをインストール

```
pip install fastapi uvicorn gunicorn
```

2. サーバ起動コマンド

```
gunicorn main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

3. ブラウザでアクセス

- http://localhost:8000/

---

開発時は、uvicorn単体でホットリロードも可能です：

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```