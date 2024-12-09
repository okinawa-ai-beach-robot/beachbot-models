from beachbot_config import config, logger
from enum import Enum
import shutil
from pathlib import Path
import os
import yaml


def load_config_file(config_path: Path = None) -> dict:
    """
    config_type: CONFIG_TYPE
    config_path: Path (Optional) use to override default config file locations with a custom one
    """

    if config_path is None:
        filename = "model_card_config.yaml"
        config_path = Path(config.BEACHBOT_CONFIG / filename)
        config_src_path = Path(BEACHBOT_OD_PATH) / "config" / filename
        logger.info(
            f"Config file not specified, using default location of {config_path}."
        )
        if not config_path.exists():
            logger.info(
                f"Config file not found at {config_path}. Copying from {config_src_path}."
            )
            # Ensure config_path parent directories exist
            config_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(config_src_path, config_path)

    # Load the YAML configuration file
    with open(config_path, "r") as file:
        config_file = yaml.safe_load(file)
    return config_file
