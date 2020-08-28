import email
import imaplib

EMAIL = 'sedosona@gmail.com'
PASSWORD = '29909060201576'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, data = mail.search(None, 'ALL')
mail_ids = []
for block in data:
    mail_ids += block.split()


def takeMSG():
    for i in mail_ids:
        status, data = mail.fetch(i, '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                print(message)
                mail_from = message['from']
                mail_subject = message['subject']
                mail_Date = message['Date']

                # print("e")
                if message.is_multipart():
                    mail_content = ''

                    # for part in message.get_payload():
                    #     # we extract it
                    #     if part.get_content_type() == 'text/plain':
                    #         mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()

                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')
                print(f'Date: {mail_Date}')
                return mail_subject


print(takeMSG())
