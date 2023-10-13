import yaml
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def send_message(message) -> None:
    msg = MIMEMultipart()
    msg['From'] = testdata['email']
    msg['To'] = testdata['email']
    msg['Subject'] = message

    with open(testdata['reportname'], 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(testdata['reportname']))
        part['Content-Disposition'] = 'attachment; filename="%s' % basename(testdata['reportname'])
        msg.attach(part)

        body = 'Error when starting a project on Python "PageObject"'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(testdata['email'], testdata['mypass'])
        text = msg.as_string()
        server.sendmail(testdata['email'], testdata['email'], text)
        server.quit()
