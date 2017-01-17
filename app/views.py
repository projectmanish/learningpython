# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:49:17 2017

@author: manish
"""

from app import app

@app.route('/')
@app.route('/index')


def index():
    return "Hello, World!"
