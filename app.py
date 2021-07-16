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
  df['Percentage'] = pd.to_numeric(df['Percentage'])
  vals = df.values[:5]
  results = dict()
  for i in range(5):
    k = dict()
    k['Ticker'] = vals[i][1]
    k['Percent'] = "{:.2f}".format(float(vals[i][0]))
    k['Amount'] = changer(amount+(amount*float(vals[i][0]))/100)
    results[i] = k
  return results

@app.route('/plot/', methods=['GET'])
def plotCalculation():
  time = str(request.args['time'])
  amount = int(request.args['amount'])
  df = pd.read_excel('Plot/'+time+'.xlsx')
  vals = df.values[:5]
  results = dict()
  for i in range(5):
    k = dict()
    k['Ticker'] = vals[i][0]
    k['Percent'] = "{:.2f}".format(float(vals[i][1]))
    k['Amount'] = changer(amount+(amount*float(vals[i][1]))/100)
    results[i] = k
  return results

def changer(amount):
	val = "{:,}".format(int(amount))
	pref = ['', 'Thousands', 'Millions', 'Billions']
	t = val.split(',')
	print(t)
	if len(t)>1:
		return t[0] + '.' + t[1][0]+' '+pref[len(t)-1]
	else:
		return t[0]
