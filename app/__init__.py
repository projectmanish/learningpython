# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:33:21 2017

@author: manish
"""


from flask import Flask

app = Flask(__name__)

from app import views
