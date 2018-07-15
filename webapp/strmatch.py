from pymongo import MongoClient
from string import ascii_lowercase
from collections import Counter
import numpy as np
import re

client = MongoClient()
db = client['test']

def getMinStringId():
    return db.strings.find_one(sort=[("string_id", 1)])["string_id"]

def getMaxStringId():
    return db.strings.find_one(sort=[("string_id", -1)])["string_id"]

def fetchStringById(sid):
    s = ""
    rec = db.strings.find_one({"string_id": sid})
    if rec:
        s = rec['string']
    return s

def matchStrings(s1=None, s2=None):
    if (s1 is None) or (s2 is None):
        return (0,0)
    lst1 = list(s1)
    lst2 = list(s2)

    # Get the count N of total matches
    N=0
    d1 = dict(Counter(lst1))
    d2 = dict(Counter(lst2))
    if " " in d1: del d1[" "] 
    if " " in d2: del d2[" "] 
    commons = set(d1.keys()).intersection(set(d2.keys()))
    for k in commons:
        N += min(d1[k], d2[k])
    
    # Get the count n1 of positional matches
    n1=0
    l = min([len(s1), len(s2)])
    for i in range(l):
        if (lst1[i] == lst2[i]):
            n1 += 1

    # Non-positional matches n2 are just N-n1
    n2 = N-n1
    return (n1, n2)

def matchStringsByIDs(sid1=None, sid2=None):
    s1 = fetchStringById(sid1)
    s2 = fetchStringById(sid2)
    return matchStrings(s1, s2)

def generateStrings(noStrings=1000, maxLength=1000, alphabet=ascii_lowercase):
    # drop current strings collection
    db.strings.drop()
  
    if not alphabet:
        print("IN strmatch.py ALPHABET IS None SETTING IT TO ascii_lowercase")
        alphabet = ascii_lowercase
    else:
        # get rid of whitespace and commas
        #alphabet = alphabet.replace(" ", "")
        alphabet = re.sub(r'[\s,]', "", alphabet)

    print("IN strmatch.py ALPHABET: ", alphabet)


    # Generate new strings (equal to noStrings) of random length of between 0 and maxLength characters, 
    # and insert them into strings collection 
    for id in range(1, noStrings+1):
        #s = "".join([ascii_lowercase[i] for i in np.random.randint(0, 26, np.random.randint(1,maxLength+1))])
        s = "".join([alphabet[i] for i in np.random.randint(0, len(alphabet), np.random.randint(1,maxLength+1))])
        #rec = { "string_id": str(id),  "length": len(s), "string": s}
        rec = { "string_id": id,  "length": len(s), "string": s}
        db.strings.insert_one(rec)
    return db.strings.find().count() 

def getLengths():
    cursor = db.strings.find()
    return [(rec['string_id'], rec['length']) for rec in cursor]

def getDistribution():
    cursor = db.strings.find()
    return Counter([rec['length'] for rec in cursor])


if __name__=="__main__":
    
    # Generate 1000 strings of max length 100
    generateStrings(1000, 100)

    # get the distribution of the strings created
    for l, n in getDistribution().items():
        print(l, n)
