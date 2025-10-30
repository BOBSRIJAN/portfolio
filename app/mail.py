import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

dotenv.load_dotenv()

def SendMail(subject: str | None, name: str| None, user_email: str | None, user_message: str | None) -> str | None:
    FROM_EMAIL = os.getenv("FROM_EMAIL")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    PASSWORD = os.getenv("PASSWORD")
    
    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = FROM_EMAIL
    message['To'] = FROM_EMAIL

    with open("app\\templates\\app\\mail\\mail.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    html_content = (
        html_template
        .replace("{{ name }}", name)
        .replace("{{ email }}", user_email)
        .replace("{{ message }}", user_message.replace("\n", "<br>"))
    )

    html_part = MIMEText(html_content, "html")
    message.attach(html_part)

    with smtplib.SMTP(HOST, PORT) as smtp:
        smtp.starttls()
        smtp.login(FROM_EMAIL, PASSWORD)
        smtp.sendmail(FROM_EMAIL, FROM_EMAIL, message.as_string())

    return "Email sent successfully!"
