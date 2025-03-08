from loguru import logger

logger.add("meu_app.log")
@logger.catch    # substitui o try/except

def somar (x: int, y: int) -> int:
    print(x)
    logger.info(x)
    logger.info(y)
    logger.info(x + y)
    return x + y

somar(2, "3")
