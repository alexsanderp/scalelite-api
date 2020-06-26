import os
import logging

assert os.getenv('SCALELITE_BIN_PATH') is not None, logging.error('Missing environment variable SCALELITE_BIN_PATH')

SCALELITE_BIN_PATH = os.getenv('SCALELITE_BIN_PATH')
