import logging

import logging.config as logconfig
import settings

logconfig.dictConfig(settings.LOGGING_PATH)

logging.debug("debug日志") #10
logging.info("info日志") #20
logging.warning("warning日志") #30
logging.error("error日志") #40
logging.critical("critical日志") #50