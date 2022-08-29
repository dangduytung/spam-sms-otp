#!/usr/bin/env python

import logging
import sys

log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s | %(name)-4s | %(levelname)-8s | %(filename)s | %(lineno)04d | %(funcName)s | %(message)s', '%m-%d-%Y %H:%M:%S')

log.disabled = True
# log.disabled = False

# Console hander
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(logging.DEBUG)
# stdout_handler.setFormatter(formatter)
# log.addHandler(stdout_handler)

# Write file log handler (Can remove this code for build product)
# file_handler = logging.FileHandler('log.txt', encoding="UTF-8")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# log.addHandler(file_handler)

# Test
# log.debug('debug')
# log.info('info')
# log.warning('warning')
# log.error('error')
# log.critical('critical')
