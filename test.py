#	-*-	coding:utf-8	-*-

import tushare as ts

# ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
# df = ts.get_latest_news(top=10) #显示最新5条新闻，并打印出新闻内容
# print df
# df.to_csv("get_latest_news.csv",encoding="gbk")
# print ts.latest_content.__doc__
a = ts.latest_content("http://finance.sina.com.cn/roll/2017-01-22/doc-ifxzutkf2272374.shtml")
b = repr(a)
b2 = eval(b[1:])
print b2
