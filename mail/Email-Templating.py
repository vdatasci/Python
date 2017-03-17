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
<p>
<img src="https://yt3.ggpht.com/-v0soe-ievYE/AAAAAAAAAAI/AAAAAAAAAAA/OixOH_h84Po/s900-c-k-no-mo-rj-c0xffffff/photo.jpg">
</p>
'''

mail.HTMLBody = Environment().from_string(TEMPLATE).render(name='Josh').strip()
mail.Send()
