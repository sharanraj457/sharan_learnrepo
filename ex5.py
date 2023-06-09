#puthon program to read a json file

import json

with open('path_to_open/ex5.json','r') as f:
     data = json.load(f)


    print(data)

