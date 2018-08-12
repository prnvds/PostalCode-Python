#===============================================================================================
#Python application that allows a user to query and show details for a given UK postcode.
#Test postcode to use: CB3 0FA (Featurespace Cambridge office)
#Created By Pranav Desai ( prnv.ds@hotmail.com )
# Time taken : 1 Hr 22 Mins
# Main Application file "test.py"
# Unittest file "apitest.py"
#===============================================================================================

import requests
import sys
import logging
import json
import re

#Setting log level to print at info level
#===============================================================================================
logging.getLogger().setLevel(logging.INFO)

# Finding country and region for given postalcode
def requestForValidPostalCode(postalCode):
    logging.info('processing postal code: %s', postalCode)
    response = requests.get("http://postcodes.io/postcodes/" + postalCode)
    logging.info('Response came back with status code: ' + str(response.raw.status))
    json_data = json.loads(response.text)
    print('Region: ' + json_data["result"]["region"] + ', Country: ' + json_data["result"]["country"])

# Finding the nearest postal codes
#===============================================================================================
def requestForNearestPostalCodes(postalCode):
    logging.info('processing postal code to retrieve nearest codes: %s', postalCode)
    response = requests.get("http://postcodes.io/postcodes/" + postalCode + "/nearest")
    logging.info('Response came back with status code: ' + str(response.raw.status))
    json_data = json.loads(response.text)
    listofNearestPostalCodes = []

    for result in json_data["result"]:
        nearestpostalCode = {}
        nearestpostalCode["postcode"] = result["postcode"]
        nearestpostalCode["region"] = result["region"]
        nearestpostalCode["country"] = result["country"]
        listofNearestPostalCodes.append(nearestpostalCode)

    print(listofNearestPostalCodes)

# Requesting user input for the postalcode. Use Python 3
#===============================================================================================
postal_code = input("Please enter valid UK postalcode: ")

#Validate user input first using UK postal code regex
#===============================================================================================
matchObj = re.match("([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z]))))\s?[0-9][A-Za-z]{2})", postal_code, re.M|re.I)
if matchObj:
    validated_response = requests.get("http://postcodes.io/postcodes/" + postal_code + "/validate")
    validated_json = json.loads(validated_response.text)
    if validated_json["result"] == True:
        requestForValidPostalCode(postal_code)
        requestForNearestPostalCodes(postal_code)
    else:
        logging.error('Entered postal code is not valid: %s', postal_code)
else:
    logging.error("User entered postcalcode is not valid")
