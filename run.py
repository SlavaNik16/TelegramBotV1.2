from loguru import logger
from bot import start_bot


def main():
    log_path = ('logs/debug.log')
    logger.add(log_path, format="{time} {level} {message}", level="DEBUG")
    start_bot()


if __name__ == '__main__':
    main()
