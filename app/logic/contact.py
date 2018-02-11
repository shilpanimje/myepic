import smtplib
import socket

from email.message import EmailMessage

msg = EmailMessage()


def send_mail(form):
    message = """From: From Person <{from_email}>
    To: To Person <{to_email}>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: {subject}

    This is an e-mail message to be sent in HTML format
    {body}
    """.format(from_email=form['email'], to_email='nimjeshilpa@gmail.com', subject=form['subject'], body=form['message'])
    sender = form['email']
    receivers = 'nimjeshilpa@gmail.com'
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(None, None)
        smtpObj.sendmail(sender, receivers, message)
        return 'test'
    except smtplib.SMTPException:
        return 'hjhkh'
