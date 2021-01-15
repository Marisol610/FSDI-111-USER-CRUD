#!/usr/bin/env python3
#-*_ coding : utf8 -*-
"""This is our app init file"""


from flask import Flask

app = Flask(__name__)

from app import routes