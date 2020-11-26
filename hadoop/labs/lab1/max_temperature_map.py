#!/usr/bin/env python

import re
import sys
import os

with open('map.out', 'a') as g:
  for path in os.listdir('c:\\users\\yelad\\Hadoop-MapReduce\\NCDC weather files'):
    print(path)
    with open('c:\\users\\yelad\\Hadoop-MapReduce\\NCDC weather files\\' + path) as f:
      lines = f.readlines()
      for line in lines:
        print(line)
        val = line.strip()
        (year, temp) = (val[15:19], val[87:92])
        if (temp != "+9999"):
          g.write("%s\t%s" % (year, temp))
