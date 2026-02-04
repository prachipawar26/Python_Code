import logging

logger = logging.getLogger(__name__)
logger.propagate = False # does not propogate to other file/module
logger.info('This is logger info message')
