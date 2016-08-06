#!/usr/bin/env python

import os
from urllib import parse

def get_env():
    return os.environ;

def get_from_url(url):
    params_section = url[url.index("?") + 1:]
    params_text = params_section.split("&")
    
    for param in params_text:
        param_split = param.split("=")

        if (len(param_split) != 2):
            print("Invalid format for param: %s" % param)
            continue

        yield _url_decode(param_split[0]), _url_decode(param_split[1])


def _url_decode(url):
    return parse.unquote(url)

params = get_from_url("index?a=x&b=y&c=z")

for p in params:
    print(p)

