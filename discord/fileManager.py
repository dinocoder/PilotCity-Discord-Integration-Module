import json
import pickle
import dill
import csv
import io
import base64
import gzip
from pprint import pprint

def readJson(fname):
    with open(fname, 'r') as f:
        return json.load(f)

def dumpJson(fname, content):
    with open(fname, 'w') as f:
        json.dump(content, f)

def appendJson(fname, data):
    f = readJson(fname)
    f.update(data)
    dumpJson(fname, f)
    

def appendListJson(fname, data):
    f = readJson(fname)
    f.append(data)
    print(f)
    print(type(f))
    dumpJson(fname, f)

def unpackObject(fname):
    with open('availableThreads/' + fname, 'rb') as f:
        obj = pickle.load(f)
        return obj

def pickleDump(path, content):
    with open(path, 'wb') as f:
            pickle.dump(content, f)

def pickleLoad_dill(path):
    with open(path, 'rb') as f:
        return dill.load(f)

def pickleDump_dill(path, content):
    with open(path, 'wb') as f:
            dill.dump(content, f)

def pickleLoad(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def appendCSV(path, content):
    with open(path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(content)

def overwriteCSV(path, content):
    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(content)
'''
def deleteCSV(path, reader):
    lines = []

    with open(path, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == members:
                    lines.remove(row)

    with open('mycsv.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
'''

def getNBTitem(location, item, value=False):
    #print(value)
    try:
        obj = location[item]
        #print('success')
    except Exception as e:
        print(e)
        return
    if value:
        #print(type(obj.value))
        return obj.value
    #print(type(obj))
    return obj

def parse_list_based_nbt(nbt_obj):
    if not nbt_obj:
        return
    obj_list = {}
    #print(nbt_obj)
    #print(type(nbt_obj))
    for i in nbt_obj:
        #print(type(i))
        obj_list[i] = getNBTitem(nbt_obj, i, value=True)
    #print(obj_list)
    return obj_list

def determine_existence(obj):
    if obj:
        return obj
    return

def zero_if_none(obj):
    if obj is None:
        return 0