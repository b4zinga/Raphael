# author: myc

from queue import Queue

from lib import ROOT_PATH
from lib.log import LoggerHandler
from lib.loader import PluginLoader


# queue
task_queue = Queue()
output_queue = Queue()

# user command line
user_args = dict()

# log
LOG_NAME = "raphael"
LOG_LEVEL = "INFO"
LOG_FILE = "logs/raphael.log"
LOG_FMT = "%(asctime)s | %(levelname)-6s| %(message)s"

logger = LoggerHandler(name=LOG_NAME, level=LOG_LEVEL, file=LOG_FILE, fmt=LOG_FMT).get_logger()

# plugin
PLUGIN_DIR = "plugins"

pl = PluginLoader(ROOT_PATH, PLUGIN_DIR)
