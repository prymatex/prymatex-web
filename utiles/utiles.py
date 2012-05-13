#! /usr/bin/python
# -*- encoding: utf-8 -*-

import re

def slugify(string):
    """ Esta funcion crea un slugfile con giones bajos """
    string = re.sub('\á','a', string)
    string = re.sub('\é','e', string)
    string = re.sub('\í','i', string)
    string = re.sub('\ó','o', string)
    string = re.sub('\ú','u', string)
    string = re.sub('\ü','u', string)
    string = re.sub('\s+', '_', string)
    string = re.sub('[^\w.-]', '', string)
    return string.strip('_.- ').lower()
