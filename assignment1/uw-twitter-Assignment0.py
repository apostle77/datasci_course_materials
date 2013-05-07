# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:40:46 2013

@author: mvillarreal
"""

#!/usr/bin/python2.7

import urllib2
import json

# retrieve recent tweets associated with the term "microsoft"

response = urllib2.urlopen("http://search.twitter.com/search.json?q=microsoft")

pyresponse = json.load(response)

results = pyresponse["results"]

for i in range(10):
 print results[i]["text"]



