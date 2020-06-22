import os
import logging
from utils import glog

APP_PATH = os.environ.get('APP_PWD')


def create_logger(log_name):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(APP_PATH+'/logs/'+log_name+'.log'),
        ])
    #download_logger = logging.getLogger('download')
    return logging.getLogger(log_name)


class BasicLogger(object):
    def __init__(self, urls):
        self.urls = urls

    def debug(self, msg):
        download_logger.debug(msg)

    def warning(self, msg):
        download_logger.warning(msg)

    def error(self, msg):
        download_logger.error(msg)
        glog.write_log('download', json.dumps({
            'url': self.urls[0],
            'status': 'error',
            'msg': msg
        }), 'ERROR')
