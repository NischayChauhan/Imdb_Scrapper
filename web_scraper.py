import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from flask import Flask, render_template, request

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
d = np.array(pd.read_csv("./a.csv"))

'''
	[
		0 
		'Frank Darabont'
		'Tim Robbins, Morgan Freeman' 
		'Two imprisoned men bond over a number of years,... on through acts of common decency.'
		'The Shawshank Redemption is a...............ly imprisoned.'
		 9.2
		'The Shawshank Redemption'
		'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGE=chttp_tt_1'
		 1994 
		 '$58,500,000' 
		 'Drama' 
		'https://m.media-amazon.com/images/M/MV82,268_AL__QL50.jpg'
	]
'''
@app.route("/")
def form():
	mov=[]
	for i in range(d.shape[0]):
		mov.append(d[i][6])
	print type(mov[0])
	return render_template('form.html', title='HOME',mov=mov,len=range(d.shape[0]))

@app.route("/movie", methods=['GET','POST'])
def movie():
	if request.method == 'POST':
		x = request.form['movie_name']
		data = []
		for i in d:
			if i[6] == x:
				data = i
		return render_template('movie.html',data=data)
	
if __name__ == "__main__":
	app.run(debug=True)