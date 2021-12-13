#!/usr/bin/python

import os
import re
from collections import Counter

log_dir = os.path.abspath(os.path.join((__file__), '../'))
file_dir = os.path.join(log_dir, 'access.log')
export_file = os.path.join(log_dir, 'export.txt')

regex1 = 'GET|POST|PUT'
regex2 = 'GET'
regex3 = 'POST'
regex4 = 'PUT'

all = 0
get = 0
post = 0
put = 0
with open(file_dir, 'r') as f:
    for i in f:
        for match in re.finditer(regex1, i, re.S):
            all += 1

with open(file_dir, 'r') as f:
    for i in f:
        for match in re.finditer(regex2, i, re.S):
            get +=1

with open(file_dir, 'r') as f:
    for i in f:
        for match in re.finditer(regex3, i, re.S):
            post += 1

with open(file_dir, 'r') as f:
    for i in f:
        for match in re.finditer(regex4, i, re.S):
            put += 1

with open(file_dir, 'r') as f:
    text = f.read()
    cnt = Counter((re.findall('(?P<url>https?://[^\s]+)', text)))
    n = cnt.most_common(10)

with open(export_file, "w+") as e:
    e.writelines(f"Requests count::n {all}\n")
    e.writelines(f"GET requests count:\n {get}\n")
    e.writelines(f"Post request count:\n {post}\n")
    e.writelines(f"PUT requests count:\n {put}\n")
    e.writelines(f"Most common requests:\n")
    for i in n:
        e.writelines(f"{i}\n")
