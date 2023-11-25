



from imap_tools import MailBox, AND, MailMessageFlags


user: str = 's@gmail.com'
password: str = ''
server: str = 'imap.gmail.com'
# Server is the address of the IMAP server
mb = MailBox(server).login(user, password)

messages = mb.fetch(criteria=AND(seen=False, from_="s@gmail.com"),
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


