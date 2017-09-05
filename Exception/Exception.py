import traceback
from Response.Response import bad_response
import logging
import datetime

from Logging.Logging import logger


class StarlingBaseException(Exception):
    def __init__(self, status_code, error_code, message):
        self.status_code = status_code
        self.status_message = message
        self.utc_time = datetime.datetime.utcnow()
        self.error_code = error_code

    def convert_to_dict(self):
        return {'status_code': self.status_code, 'status_message': self.status_message, 'time': self.utc_time.isoformat() }

class StarlingEmployerDataNotLoadException(StarlingBaseException):
    def __init__(self, message):
        super().__init__(400, 1000, message)

class StarlingRunTimeException(Exception):
    def __init__(self):
        self.status_code = 400
        self.status_message = "Starling Error"
        self.utc_time = datetime.datetime.utcnow()
        self.error_code = 500

    def convert_to_dict(self):
        return {'status_code': self.status_code, 'status_message': self.status_message,
                'time': self.utc_time.isoformat()}

def deal_with_exception(e):

    if isinstance(e, StarlingBaseException):
        logger.error('simple-api-error: {}'.format(e))
        return bad_response(e.convert_to_dict())

    logger.exception('simple-api-exception: {}'.format(e))
    return bad_response(StarlingRunTimeException().convert_to_dict())
