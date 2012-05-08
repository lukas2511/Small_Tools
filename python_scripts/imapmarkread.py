import imaplib

server=''
ssl=0
user=''
passwd=''
path='INBOX'

if ssl:
    mail = imaplib.IMAP4_SSL(server)
else:
    mail = imaplib.IMAP4(server)

mail.login(user, passwd)

mail.select(path)

result, data = mail.uid('search', None, "ALL")

ids=data[0]
id_list = ids.split()

for id in id_list:
    mail.uid('store', id, '+FLAGS', '(\\Seen)')

print "executing deletion"
mail.expunge()
print "done"
