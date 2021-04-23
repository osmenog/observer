import logging
import signal
import sys

from .httpd import init_httpd
from .observer import Observer

logger = logging.getLogger(__name__)


def init_logging():
    """ Настройка логирования """
    log_format = '[%(asctime)23s] [%(process)d] [%(threadName)s] [%(name)s] %(message)s'
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(log_format))

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)

    logging.getLogger("urllib3").propagate = False
    logging.getLogger("requests").propagate = False


def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)


def main():
    """ Точка входа """

    signal.signal(signal.SIGTERM, sigterm_handler)

    # Настраиваем логирование
    init_logging()

    # Инициализируем основной компонент
    ob = Observer()

    init_httpd()

    try:
        logger.info('[*] Observer was started!')
        ob.start()  # Запускаем обозреватель

    except KeyboardInterrupt:
        # Обрабатываем ручное прерывание работы программы
        ob.terminate()
        logger.info('[*] Observer was interrupted.')