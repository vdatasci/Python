from pandas import *
import numpy

data = {
        'name': ['UConn','NorthWestern','Harvard','Yale','MIT'],
        'year': [2016,2012,2013,2014,2016],
        'reports': [1,24,31,2,3]
        }

df = pandas.DataFrame(data, index = ['index1','index2','index3','index4','index5'])
df

#export DataFrame to HTML file

df.to_html('C:\df__to_HTML.html')

