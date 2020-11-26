#!/usr/bin/env python

import sys
import math

(last_key, max_val) = (None, -math.inf)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  if last_key and last_key != key:
    print(f"{last_key}\t{max_val}")
    (last_key, max_val) = (key, int(val))
  else:
    (last_key, max_val) = (key, max(max_val, int(val)))

if last_key:
  print("%s\t%s\n" % (last_key, max_val))