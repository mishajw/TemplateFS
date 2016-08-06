#!/usr/bin/env python

import os
from urllib import parse

def get_all_variables(url
    return {**get_env(), **get_from_url(url)}

def get_env():
    return os.environ;


def get_from_url(url):
    if "?" not in url:
        return {}
    
    return dict(_get_from_url_generator(url))

def _get_from_url_generator(url):
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

