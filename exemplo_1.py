from utils_log import log_decorator

@log_decorator

def somar (x: int, y: int) -> int:
    return x + y

somar(2, 3)
somar(2, 7)
