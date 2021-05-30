import pandas as pd
import numpy as np
import datetime
from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/stock/', methods=['GET'])
def stockCalculation():
  time = str(request.args['time'])
  amount = int(request.args['amount'])
  df = pd.read_excel('Stock/'+time+'.xlsx')
  vals = df.values[:5]
  results = []
  for i in range(5):
    k = dict()
    k['Ticker'] = vals[i][1]
    k['Percent'] = vals[i][0]
    k['Amount'] = amount+(amount*float(vals[i][0]))/100
    results.append(k)
  return results

@app.route('/plot/', methods=['GET'])
def plotCalculation():
  time = str(request.args['time'])
  amount = int(request.args['amount'])
  df = pd.read_excel('Plot/'+time+'.xlsx')
  vals = df.values[:5]
  results = []
  for i in range(5):
    k = dict()
    k['Ticker'] = vals[i][1]
    k['Percent'] = vals[i][0]
    k['Amount'] = amount+(amount*float(vals[i][0]))/100
    results.append(k)
  return results
