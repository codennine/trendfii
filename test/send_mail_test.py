import smtplib, ssl, os, sys
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from dotenv import load_dotenv
load_dotenv()

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_TO = os.getenv('EMAIL_TO')
FROM_NAME = os.getenv('FROM_NAME')

# Create a secure SSL context
context = ssl.create_default_context()

msg = MIMEMultipart()
msg['From'] = '{}, <{}>'.format(FROM_NAME, EMAIL_FROM)
msg['To'] = EMAIL_TO
msg['Subject'] = 'Email com anexo 2'
# body = 'Testando coisas com python em texo'
body_html = 'Testando envio de anexo no e-mail'
# msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(body_html, 'html'))

filename = 'data.json'

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
  # Add file as application/octet-stream
  # Email client can usually download this automatically as attachment
  # part = MIMEBase("application", "octet-stream")
  # part.set_payload(attachment.read())
  part = MIMEBase("text", "json")
  part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

part.add_header(
  "Content-Disposition",
  "attachment; filename= {filename}".format_map({'filename': filename}),
)

msg.attach(part)

text = msg.as_string()

try:
  server = smtplib.SMTP(smtp_server,port)
  server.ehlo() # Can be omitted
  server.starttls()
  server.ehlo() # Can be omitted
  server.login(EMAIL_USER, EMAIL_PASSWORD)
  server.sendmail(EMAIL_FROM, EMAIL_TO, text)
  # TODO: Send email here
except Exception as e:
  # Print any error messages to stdout
  # print(e)
  exc_type, exc_obj, exc_tb = sys.exc_info()
  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
  print(exc_type, fname, exc_tb.tb_lineno)
finally:
  server.quit()