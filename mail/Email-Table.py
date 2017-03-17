from jinja2 import Environment
import win32com.client as win32
from pandas import *



data = {
        'name': ['UConn','NorthWestern','BSU','Yale','MIT'],
        'year': [2016,2012,2013,2014,2016],
        'reports': [1,24,31,2,3]
        }

df = pandas.DataFrame(data, index=None)


outlook = win32.Dispatch('outlook.application')
inbox = outlook.GetNamespace("MAPI").GetDefaultFolder(6)
messages = inbox.Items
last_message = str(messages.GetLast())
last_message_body_content = last_message.body



mail = outlook.CreateItem(0)
mail.TO = 'joshvoss90@outlook.com'
mail.Subject = 'test'
mail.Body = 'Message Body'



TEMPLATE = '''
<h1>Your Table:</h1>
<p> {{dftable | safe}} </p>
<p>{last_message} p2</p>
'''

mail.HTMLBody = Environment().from_string(TEMPLATE).render(dftable=df.to_html(index=False)).strip()
mail.Send()
