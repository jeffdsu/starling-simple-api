import json
from flask import Response

from Logging.Logging import logger

def good_response(json_data):
    logger.info('simple-api-resp: {}'.format(json.dumps(json_data)))
    return Response(
            response=json.dumps(json_data, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=200,
            mimetype='application/json'
        )

def good_data_response(json_data):
    logger.info('simple-api-resp: {}'.format(json.dumps(json_data)))
    return Response(
            response=json.dumps({'data': json_data}, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=200,
            mimetype='application/json'
        )

def bad_response(json_data):

    logger.info('simple-api-bad-resp: {}'.format(json.dumps(json_data)))

    return Response(
            response=json.dumps(json_data, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=400,
            mimetype='application/json'
        )