import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('juliencorioux@gmail.com', 'password')
fromaddr = 'FooFight <juliencorioux@gmail.com>'
toaddrs = ['lefatoum@hotmail.fr']
sujet = "Reunion"
message = u"""\

Rappelez , c'est important !

"""
msg = """\
From: %s\r\n\
To: %s\r\n\
Subject: %s\r\n\
\r\n\
%s
""" % (fromaddr, ", ".join(toaddrs), sujet, message)
try:
    server.sendmail(fromaddr, toaddrs, msg)
except smtplib.SMTPException as e:
    print(e)
server.quit()
