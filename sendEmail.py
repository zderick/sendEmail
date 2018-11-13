# import yagmail

# contents = [
#     "This is the body, and here is just text",
#     "Second line here"
# ]

# yag = yagmail.SMTP('from@gmail.com', "*****")
# yag.send('to@gmail.com', 'subject', contents)


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.header import Header

from email.MIMEText import MIMEText
from email.utils import formataddr
 
fromaddr = "lynlynlynt@gmail.com"
toaddr = ['to@gmail.com']
fakeCcList = ['fakecc@gmail.com']
bccList = ['bcc@gmail.com']
msg = MIMEMultipart()

msg['From'] = formataddr((str(Header('First Last', 'utf-8')), fromaddr))
msg['To'] = ",".join(toaddr)
msg['Cc'] = ",".join(fakeCcList)
msg['Subject'] = "Subject"
msg.add_header('reply-to', "replyto@gmail.com")
 
body = "Message"
msg.attach(MIMEText(body, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, bccList + toaddr, text)
server.quit()
