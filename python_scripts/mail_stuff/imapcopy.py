import imaplib
import time

sourceserver=''
sourcessl=0
sourceuser=''
sourcepasswd=''
sourcepath='INBOX'

targetserver=''
targetssl=0
targetuser=''
targetpasswd=''
targetpath='INBOX'

if sourcessl:
    smail = imaplib.IMAP4_SSL(sourceserver)
else:
    smail = imaplib.IMAP4(sourceserver)

smail.login(sourceuser, sourcepasswd)

if targetssl:
    tmail = imaplib.IMAP4_SSL(targetserver)
else:
    tmail = imaplib.IMAP4(targetserver)

tmail.login(targetuser, targetpasswd)

smail.select(sourcepath)

result, data = smail.uid('search', None, "ALL")

ids=data[0]
id_list = ids.split()

for id in id_list:
    result, data = smail.uid('fetch',id,'(RFC822)')
    print data[0][0]
    status = tmail.append(targetpath, '', imaplib.Time2Internaldate(time.time()), str(data[0][1]))
    print status
