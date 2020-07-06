import json
filename="./dblist"


with open(filename) as f:
    str=f.read().replace("]", "],")
    #dict=json.loads(str)
    print(str)