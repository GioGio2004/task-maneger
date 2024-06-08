
import smtplib


password = "password gmail key"


email = "examplesender@gmail.com"
reciever_email = "examplerecipiemt@gmail.com"
subject = "new task"
message = "hello"


text = f"Subject: {subject}\n\n {message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

def send_email(text):
    server.login(email, password)
    server.sendmail(email, reciever_email, text)

print(f"mail has been sent to {reciever_email}")
