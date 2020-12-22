import smtplib, ssl, os, sys
from datetime import datetime
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

if __name__ == "__main__":
  from dotenv import load_dotenv
  load_dotenv()

SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = os.getenv('SMTP_PORT', 587) 
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_mail(email_from, to, subject, body_message, from_name=None):
  TODAY = datetime.utcnow()
  # Create a secure SSL context
  context = ssl.create_default_context()
  from_str = '{} <{}>'.format(from_name, email_from) if not from_name is None else email_from 
  msg = MIMEMultipart()
  msg['From'] = from_str
  msg['To'] = to
  msg['Subject'] = subject
  body_html = body_message
  msg.attach(MIMEText(body_html, 'html'))
  text = msg.as_string()
  server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
  server.ehlo() # Can be omitted
  server.starttls()
  server.ehlo() # Can be omitted
  server.login(EMAIL_USER, EMAIL_PASSWORD)
  server.sendmail(email_from, to, text)
  server.quit()


if __name__ == '__main__':
  send_mail('projetoscodesilva@gmail.com', 'edigleyssonsilva@gmail.com', 'Generico', '<h1>hello</h1>', 'Projetos Codesilva')