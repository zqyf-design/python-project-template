from src.logger import setup_logger
from src.config import Config
from src.utils import greet, add, multiply

logger = setup_logger(__name__)


def main():
    logger.info(f"Starting {Config.APP_NAME}")
    logger.debug(f"Debug mode: {Config.DEBUG}")

    message = greet("World")
    logger.info(message)

    result = add(10, 20)
    logger.info(f"10 + 20 = {result}")

    result = multiply(5, 6)
    logger.info(f"5 * 6 = {result}")

    logger.info("Application finished successfully")


if __name__ == "__main__":
    main()