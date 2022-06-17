 
import os
import json
import time
from routes.api import api

# runs on schedule OR on route request
def task():
  print('doing task')
  api_response = api()
  # our storage file
  dir = './data'
  file = './data/my.json'
  # if it doesn't exist, create one
  
  if not os.path.exists(dir):
    print("file doesn't exist")
    os.mkdir(dir)
    with open(file, 'w') as f: 
      f.write(json.dumps([]))
  # open the file and add the api response
  with open(file, 'r+') as readFile: 
    # read file, deserialize it, append api response
    deserial = json.load(readFile)
    # add time stamp
    api_response['time'] = time.time()
    print(api_response)
    deserial.append(api_response)
    readFile.seek(0)
    serialize = json.dumps(deserial, indent=2)
  # open the file and write the appended api response
  f = open(file, 'w')
  f.write(serialize)
  f.close()
  # if execution context is template, return response there
  return api_response