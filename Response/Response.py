import json
from flask import Response

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def good_response(json_data):

    return Response(
            response=json.dumps(json_data, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=200,
            mimetype='application/json'
        )

def good_data_response(json_data):

    return Response(
            response=json.dumps({'data': json_data}, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=200,
            mimetype='application/json'
        )

def bad_response(json_data):

    print("asdfasd")

    return Response(
            response=json.dumps(json_data, sort_keys=True,
                indent=4, separators=(',', ': ')),
            status=400,
            mimetype='application/json'
        )