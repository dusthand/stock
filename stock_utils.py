# -*- coding:utf-8 -*-

import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

PATH = "csv/%s.csv"



def print_stock_fig(code,save = "True"):
	df = try_get_hist_data(code)
	df.to_csv(PATH%code)
	df = df.sort(ascending="False")
	df.plot(y=["ma5"])
	plt.show()

def try_get_hist_data(code):
	df = None
	try:
		df = pd.read_csv(PATH%code)
		df = df.set_index("date")
		# print "use cache:"+code
	except:
		# print "use remote:"+code
		df = ts.get_hist_data(code)
		if df is not None:
			df.to_csv(PATH%code)
		else:
			print "error:"+code
	return df


def get_top_fund_holdings(y,q,nums=50):
	path = PATH%("fund_holdings_%s_%s"%(y,q))
	try:
		df = pd.read_csv(path)
	except:
		df = ts.fund_holdings(y,q)
		df.to_csv(PATH%(path),encoding = "gbk")
		df = pd.read_csv(path)
	df = df.sort(["nums"],ascending=False)
	df =  df["code"]
	top_50 =  list(df.head(nums))
	top_50 = [ str(x).zfill(6) for x in top_50]
	return top_50


def get_top_fh_data():
	import time
	tops = get_top_fund_holdings(2016,1,50)
	for code in tops:
		try_get_hist_data(code)
		time.sleep(1)

def get_top_fh_stock_means():
	tops = get_top_fund_holdings(2016,4,20)
	a = [ [0,0] for i in range(800)]
	x = None
	for code in tops:
		df = try_get_hist_data(code)
		se = df["ma5"]
		# se = se.head(2)
		# print code
		# print se
		vs = se.values
		if x == None:
			x =  list(se.axes[0].values)
			x.reverse()
		# print len(vs)
		means = float(sum(vs)) / len(vs)
		for i in xrange(len(vs)):
			# print i
			if vs[i]>0:
				a[i][0] = a[i][0]+vs[i]/means
				a[i][1]+=1

	# return		
		# if 
	a = [d[0]/d[1] for d in a if d[1]>0]
	a.reverse()
	mins = min(len(a),len(x))
	# print plt.plot.__doc__

	pd.Series(a[0:mins],x[0:mins]).plot()
	plt.title(u'被持有最多的股票前20名平均值')
	# a.plot(title= "前50名股票的平均")
	# print plt.legend.__doc__
	df = try_get_hist_data("sh")
	df = df.sort_index(ascending=True)
	df.plot(y=["ma5"])

	
	plt.show()

def get_news_content_by_url(url):
	a = ts.latest_content(url)
	b = repr(a)
	b2 = eval(b[1:])
	return b2



if __name__ == "__main__":
	get_top_fh_stock_means()
	# print str(7).zfill(5)

# if __name__ =="__main__":
# 	a = pd.read_csv("600848.csv")
# 	print a.columns
# 	a = a.set_index(["date"])
	

# 	a.plot(y=["high","low","ma5"])
# 	plt.show()
# 	# print dir(pd)