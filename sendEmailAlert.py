#python -m smtpd -c DebuggingServer -n localhost:1025

import smtplib

smtpUser = 'aditya.agashe1234@gmail.com'
smtpPass = 'sticktoyisdead!24'

toAdd = 'aditya.agashe1997@gmail.com'
fromAdd = smtpUser

subject = 'Raspberry pi test alert email'
header = 'To: '+ toAdd + '\n'+'From: ' + fromAdd + '\n' + 'Subject: ' +  subject 
body = "Test mail form Raspberry pi using  python. ALERT WARNING"

print (header + '\n' + body)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n'+body)

s.quit()
