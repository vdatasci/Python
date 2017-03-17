from jinja2 import Environment
import win32com.client as win32
from pandas import *



data = {
        'name': ['UConn','NorthWestern','BSU','Yale','MIT'],
        'year': [2016,2012,2013,2014,2016],
        'reports': [1,24,31,2,3]
        }

df = pandas.DataFrame(data, index=False)


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.TO = 'joshvoss90@outlook.com'
mail.Subject = 'test'
mail.Body = 'Message Body'



TEMPLATE = '''
<h1>Your Table:</h1>
<p> {{dftable | safe}} </p>
'''

mail.HTMLBody = Environment().from_string(TEMPLATE).render(dftable=df.to_html()).strip()
mail.Send()
