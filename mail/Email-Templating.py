from jinja2 import Environment
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.TO = 'joshvoss90@outlook.com'
mail.Subject = 'test'
mail.Attachments.Add(Source='F:\Images\pointers.png')
mail.Body = 'Message Body'


TEMPLATE = '''
<b> {{name}} </b>
'''

mail.HTMLBody = Environment().from_string(TEMPLATE).render(name='Josh').strip()
mail.Send()
