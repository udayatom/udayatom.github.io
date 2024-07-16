import ssl
import urllib.request

import pandas as pd
import numpy as np
from urllib.request import Request, urlopen
import json
import json
profileinfotillT = []


def generateList():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for i in range(307, 450):
        webpage = urllib.request.urlopen("https://nammaoorutv.com/dashboard/api.php?type=advertisment&ch_id="+str(i),context=ctx).read()
        print("https://nammaoorutv.com/dashboard/api.php?type=advertisment&ch_id=" + str(i))
        profileinfotillT.append({f'{i}': json.loads(webpage)})
        # loadinstring += str(i) + " completed"


def processData():
    input_file = open('scrappeddata.json')
    json_array = json.load(input_file)
    channel_list = []
    for i in range(0,len(json_array)):
        item = list(json_array[i].values())[0]
        channel_list.append({"name":item["channel_name"],"url":item["streaming_url"],"favicon":item["channel_logo"]})
    print(channel_list)

#generateList()
processData()
print(profileinfotillT)
