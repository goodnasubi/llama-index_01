# Copyright (c) 2024 Your Name or Organization

import logging
import logging.config
from pathlib import Path

import yaml


def setup_logger(name: str | None = None) -> logging.Logger:
    """YAML形式のロギング設定を読み込み、指定名のloggerを返す.

    Returns:
        logging.Logger: 指定名のロガーインスタンス。

    """
    config_path = Path(__file__).parent / "logging.yaml"
    with config_path.open(encoding="utf-8") as f:
        config = yaml.safe_load(f)
    logging.config.dictConfig(config)
    return logging.getLogger(name)


logger = setup_logger(__name__)
