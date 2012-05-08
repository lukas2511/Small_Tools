import imaplib
import hashlib

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

mails = []

for id in id_list:
    result, data = mail.uid('fetch',id,'(RFC822)')
    hash = hashlib.sha1(data[0][1]).hexdigest()
    try:
        dupid=mails.index(hash)
	print "removing duplicate %s (duplicate of %s)" % (id,dupid)
        mail.uid('store',id, '+FLAGS', '(\\Deleted)')
    except ValueError:
        mails.append(hash)
        print "%s is not a duplicate" % id

print "executing deletion"
mail.expunge()
print "done"
