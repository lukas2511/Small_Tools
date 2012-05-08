import imaplib

server=''
ssl=0
user=''
passwd=''

if ssl:
    mail = imaplib.IMAP4_SSL(server)
else:
    mail = imaplib.IMAP4(server)

mail.login(user, passwd)

list = mail.list()[1]

for box in list:
    print box.split(' "." ')[1]
