#
# import imaplib, string, email
# M = imaplib.IMAP4_SSL("imap.gmail.com")
# print (M)
# try:
#     try:
#         M.login('sermatrena@gmail.com','Sereja123')
#         print('подключился к почте')
#     except Exception as e:
#         print ('login error: %s' % e)
#         M.close()
#     M.select()
#     result, message = M.select()
#     typ, data = M.search(None, 'ALL')
#     for num in string.split(data[0]):
#         try:
#             typ, data = M.fetch(num, '(RFC822)')
#             msg = email.message_from_string(data[0][1])
#             print (msg["From"])
#             print (msg["Subject"])
#             print (msg["Date"])
#             print ("_______________________________")
#         except Exception as e:
#             print ('got msg error: %s' % e            )
#     M.logout()
#     M.close()
# except Exception as e:
#     print ('imap error: %s' % e)
#     M.close()

from imap_tools import MailBox, AND, MailMessageFlags

user: str = '11111@gmail.com'
password: str = '1111'
server: str = 'imap.gmail.com'
# Server is the address of the IMAP server
mb = MailBox(server).login(user, password)

messages = mb.fetch(criteria=AND(seen=False, from_="1111@gmail.com"),
                    mark_seen=False,
                    bulk=True)

uids = []

for msg in messages:
    # Print form and subject
    print(msg.from_, ': ', msg.subject)
    # Print the plain text (if there is one)
    print(msg.text)

    # Add attachments
    for att in msg.attachments:
        with open(f'{att.filename}', 'wb') as f:
            f.write(att.payload)

    uids.append(msg.uid)

with MailBox(server).login(user, password, 'INBOX') as mailbox:
    mailbox.flag(uids, MailMessageFlags.SEEN, True)
