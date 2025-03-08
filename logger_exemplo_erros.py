from loguru import logger

print("essa mensagem significa:")

# principais
logger.debug("Um aviso para um desenvolvedor (ou em mesmo) no futuro")
logger.info("Uma informacao importante do processo")
logger.warning("Um aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma falha que aborta a aplicação")

#gostei
logger.success("Uma operação foi concluída com êxito")
logger.exception("Registra uma exceção com traceback")
logger.catch("Captura exceções automaticamente")
#logger.level("Define ou altera níveis de log")

#outros
logger.trace("Um nível abaixo de DEBUG, útil para rastreamento detalhado")
#logger.bind("Adiciona contexto extra aos logs")
#logger.complete("Executa uma ação ao finalizar um bloco")
#logger.configure("Modifica a configuração global do logger")
#logger.contextualize("Cria um logger com contexto específico")
logger.disable("Desativa temporariamente o logger")
logger.enable("Reativa o logger após desativação")
#logger.log("Registra uma mensagem com nível personalizado")
#logger.opt("Fornece opções extras para o log")
#logger.parse("Analisa strings para criar mensagens de log")
logger.patch("Modifica dinamicamente o comportamento do logger")
#logger.remove("Remove um manipulador de log")
#logger.start("Inicia um novo processo de log")
#logger.stop("Para um processo de log ativo")


@logger.catch
def dividir(a, b):
    return a / b

dividir(10, 0)  # O Loguru capturará e registrará a exceção automaticamente