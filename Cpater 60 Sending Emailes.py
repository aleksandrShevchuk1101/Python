from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path


html_templ = Template(Path('templates/template.html').read_text())

print(html_templ)

html_content = html_templ.substitute({'name': 'Bogdan', 'date': 'tommorow'})

my_email = EmailMessage()
print(type(my_email))

my_email['from'] = 'Bogdan'
my_email['to'] = 'test@test.com'
my_email['subject'] = "Hello from Python"

my_email.set_content(html_content, 'html')


with smtplib.SMTP(host="127.0.0.1", port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print('Email was send')
