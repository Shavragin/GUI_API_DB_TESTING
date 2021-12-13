import os
import re
from collections import Counter

log_dir = os.path.abspath(os.path.join((__file__), '../'))
file_dir = os.path.join(log_dir, 'access.log')

regex1 = 'GET|POST|PUT'
regex2 = 'GET'
regex3 = 'POST'
regex4 = 'PUT'


def get_calls_quantity():
    all = 0
    with open(file_dir, 'r') as f:
        for i in f:
            for _ in re.finditer(regex1, i, re.S):
                all += 1
        return all


def obtain_type_quantity():
    get = 0
    post = 0
    put = 0
    with open(file_dir, 'r') as f:
        for i in f:
            for _ in re.finditer(regex2, i, re.S):
                get += 1

    with open(file_dir, 'r') as f:
        for i in f:
            for _ in re.finditer(regex3, i, re.S):
                post += 1

    with open(file_dir, 'r') as f:
        for i in f:
            for _ in re.finditer(regex4, i, re.S):
                put += 1

    return get, post, put


def most_callable_url():
    with open(file_dir, 'r') as f:
        text = f.read()
        cnt = Counter((re.findall('(?P<url>https?://[^\s]+)', text)))
        most_common = cnt.most_common(10)
        return most_common


def most_5_4xx_url():
    with open(file_dir, 'r') as f:
        l = []
        for line in f.readlines():
            split_line = line.split()
            if re.fullmatch('4\d{2}', split_line[8]) is not None:
                l.append(line)
        l.sort(key=lambda x: x.split()[9], reverse=True)
        b = 0
        result = []

        for i in l:
            d = i.split()
            request_summary = (d[6].split('://')[-1], d[8:10], d[0])
            result.append(request_summary)

            if b >= 4:
                break
            b += 1
    return result


def most_5_5xx_ip():
    with open(file_dir, 'r') as f:
        errors = []
        for line in f.readlines():
            split_line = line.split()
            if re.fullmatch('5\d{2}', split_line[8]) is not None:
                errors.append(line)
        ips = []
        for i in errors:
            ip = i.split()[0]
            ips.append(ip)
        most_common_5 = Counter(ips).most_common(5)
        return most_common_5
