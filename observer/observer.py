import logging
from time import sleep

logger = logging.getLogger(__name__)


class Observer:
    def __init__(self, args=None):
        self.args = args

    def start(self):
        # Стартуем бесконечный цикл.
        while True:
            sleep(1)
            logger.debug('tick')

    def terminate(self):
        pass
