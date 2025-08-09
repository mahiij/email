import smtplib

email = input("SENDER EMAIL:" )
recevier_email=input("RECEIVER EMAIL: ")

subject = input("Subject: ")
message = input("Message: ")

text=f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email,"baaujhjujlhssfpt")
server.sendmail(email,recevier_email,text)
print("Email sent Successfully!")