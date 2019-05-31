#functions.py
import json


#checking if pingdom_checks table exists in the tables argument
#return true if does
def does_pingdom_checks_exists(tables):
    searchvalue = "pingdom_checks"
    for item in tables:
        if(searchvalue in item):
            return True
    return False


def read_json_data():
    with open('sample.json') as json_file:  
        data = json.load(json_file)
        localData = Database(data)
        print(localData.adattar[1])