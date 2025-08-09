import smtplib

# Sender details
sender_email = "mahithajangala008@gmail.com"
sender_password = "baaujhjujlhssfpt"  # NOT your normal Gmail password

# List of recipients
recipients = [
    "22BQ1A4922@vvit.net",
    "24BQ1A5468@vvit.net",
    "22BQ1A4904@vvit.net",
    "jangalamahitha@gmail.com",
    "beerasamba@gmail.com"
]

# Email content
subject = "Test Bulk Email"
message = "Hello! This is a bulk email test from Python."
email_text = f"Subject: {subject}\n\n{message}"

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login with your Gmail and App Password
server.login(sender_email, sender_password)

# Send email to each recipient
for recipient in recipients:
    server.sendmail(sender_email, recipient, email_text)
    print(f"Email sent to {recipient}")

# Close connection
server.quit()

print("All emails sent successfully!")
