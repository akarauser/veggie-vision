import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from ._logger import logger


class ConfigValidation(BaseModel):
    base_dir: str
    output_dir: str
    batch_size: int
    image_size: list
    seed: int
    base_learning_rate: float


def _read_json_file() -> Any | None:
    config_path = Path(f"{Path(__file__).parent}\\config.json")
    try:
        with config_path.open(encoding="utf-8") as file:
            config_values = json.load(file)
            return config_values
    except FileNotFoundError:
        logger.error("Config file not found.")


try:
    config_args = ConfigValidation.model_validate(_read_json_file())
except ValueError:
    logger.error("Validation failed.")
