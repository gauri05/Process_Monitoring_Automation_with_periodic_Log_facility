import urllib3
from sys import *
import time
import smtplib


def is_connected():
    try:
        urllib3.connectionpool.connection_from_url('http://216.58.192.142 ', timeout=1)
        # urllib3.connection_from_url('https://www.google.com/ ',timeout=1)   #https://www.google.com/   #http://216.58.192.142
        return True
    except urllib3.URLError as err:
        return False

def MailSender(gmail_user,gmail_pass):
    send_from=gmail_user
    to=['gauribotre50@gmail.com']

    email_text="Welcome........."

    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user,gmail_pass)
        server.sendmail(send_from,to,email_text)
        server.close()

        print("Mail Sent Successfully....")
    except Exception as E:
        print("Unable to sent mail",E)

def main():
    print("Mail Sending....")
    print("Application name:" + argv[0])
    try:
        gmail_user='botregauri@gmail.com'
        gmail_password='3796gouri'

        conected=is_connected()

        if conected:
            starttime=time.time()
            MailSender(gmail_user,gmail_password)
            endtime=time.time()

            print('Took %s seconds to send mail' % (endtime - starttime))
        else:
            print("There is no internet connection...")

    except Exception as E:
        print("Error : Invalid input", E)


if __name__ == "__main__":
    main()
