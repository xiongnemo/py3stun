from .pystun import get_ip_info
from .cli import main

import logging

__version__ = '0.1.0'

log = logging.getLogger('pystun')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s.%(funcName)s - %(levelname)s - %(message)s')

