import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Sherlock'
email['to'] = 'chowdharyanshuman007@gmail.com'
email['subject'] = 'You won 110000100001 dollars'

email.set_content(html.substitute({'name':'Tintin'}))
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
