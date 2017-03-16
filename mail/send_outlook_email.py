#requirements: 
#pip install pypiwin32

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.TO = 'email@address.com'
mail.Subject = 'Subject Text'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>'# this field is optional
mail.Send()
