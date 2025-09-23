# Copyright (c) 2024 Your Name or Organization


from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.readers.web import BeautifulSoupWebReader

from logger_setup import logger

load_dotenv()


def simple_web_reader(urls: list[str]) -> list:
    logger.info("Webからデータ取得開始")
    reader = BeautifulSoupWebReader()
    return reader.load_data(urls)


def create_index() -> VectorStoreIndex:
    """最新のVectorStoreIndexを作成して返す.

    Returns:
        VectorStoreIndex: 最新のVectorStoreIndexインスタンス。

    """
    # LLMの設定(OpenAI APIキーは環境変数で設定)
    logger.info("インデックス作成開始")
    llm = OpenAI(model="gpt-5-nano")

    # Webからデータ取得
    urls = ["https://www.exiis-lab.com/"]
    documents = simple_web_reader(urls)

    # 最新のVectorStoreIndexでインデックス作成
    return VectorStoreIndex.from_documents(documents, llm=llm)
