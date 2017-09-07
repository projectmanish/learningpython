import json
import yaml

import logging
import numpy as np
from sklearn.cluster import KMeans
import itertools
import pandas as pd
import multiprocessing as mp
#import dask.dataframe as dd
#import pandas.io.sql as psql
import cx_Oracle
import csv
import sys
import os
import time
from time import sleep
from random import randint
from math import sqrt


#http://www.juliandyke.com/Research/Development/UsingPythonWithOracle.php
#https://stackoverflow.com/questions/40357434/pandas-df-iterrow-parallelization
#https://stackoverflow.com/questions/43360077/using-multiprocessing-with-pandas-dataframe
#https://www.binpress.com/tutorial/simple-python-parallelism/121
#https://sedeh.github.io/python-pandas-multiprocessing-workaround.html
#https://stackoverflow.com/questions/39944824/python-multiprocessing-simple-job-split-across-many-processes
#https://www.irs.gov/pub/irs-soi/?C=N;O=D
#http://sebastianraschka.com/Articles/2014_multiprocessing.html
#http://python.omics.wiki/multiprocessing_map/multiprocessing_partial_function_multiple_arguments
#https://gist.github.com/baojie/6047780
#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

logging.basicConfig(filename='c:/churn_error.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)


def printf (format,*args):
  sys.stdout.write (format % args)

def printException (exception):
  error, = exception.args
  printf ("Error code = %s\n",error.code);
  printf ("Error message = %s\n",error.message);
  
def create_conn(connection):
    oracle_conn =  cx_Oracle.connect(connection)
    return oracle_conn

results = []

def collect_results(result):
    """Uses apply_async's callback to setup up a separate Queue for each process"""
    results.append(result)




critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
        
    if len(si)==0:
        return 0
    
#    sum_of_squares = sum(pow(prefs[person1][item]-prefs[person2][item],2)  for item in prefs[person1] if item in prefs[[person2]] )
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    
    return 1/(1+sum_of_squares)
    
    
sim_distance(critics,'Lisa Rose','Gene Seymour')
    
