import smtplib as smtp
import ssl


def send_email(receiver_email, message):
    host = "smtp.gmail.com"
    port = 465

    user = "rippernobbsoriginal@gmail.com"
    password = "mbyj onrp dqyc rhft"

    context = ssl.create_default_context()

    message = f"""\
Subject: New email from {receiver_email}
From: {receiver_email}

{message}
"""

    with smtp.SMTP_SSL(host, port, context=context) as server:
        server.login(user, password)
        server.sendmail(user, user, message)

