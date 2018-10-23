import smtplib
import getpass

myemail=input("your email id:")
passward=getpass.getpass()
recemail=input("recevier's email id :")

# creats SMPT session
s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

# Authentication
s.login(myemail,passward)

#message to be send 
message ="hi rabi  how r u    "

#sending the mail
s.sendmail(myemail,recemail,message)

#terminating the session
s.quit()
