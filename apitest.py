# unittest code
# Created by Pranav Desai
# prnv.ds@hotmail.com




import io
import sys
import requests
import logging
import json
import re

def requestForValidPostalCode(postalCode):
    logging.info('processing postal code: %s', postalCode)
    response = requests.get("http://postcodes.io/postcodes/" + postalCode)
    logging.info('Response came back with status code: ' + str(response.raw.status))
    json_data = json.loads(response.text)
    print('Region: ' + json_data["result"]["region"] + ', Country: ' + json_data["result"]["country"])


def requestForValidPostalCodeTest():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    requestForValidPostalCode("m32 0jg")
    sys.stdout = sys.__stdout__                   # Reset redirect.
    print (capturedOutput.getvalue())             # Now works as before.

requestForValidPostalCodeTest()
