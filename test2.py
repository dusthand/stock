# -*- coding:utf-8 -*-
import tushare as ts
df = ts.get_sina_dd('600848', date='2017-1-20') #默认400手
print df