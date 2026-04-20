import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER = "szczjr@gmail.com"
APP_PASSWORD = "muzk jdcx qsqz maix"
RECIPIENTS = ["szczjr@gmail.com"]

# Optional: override subject via command-line argument
subject = sys.argv[1] if len(sys.argv) > 1 else "Praha 10 Newsletter"

with open("digest.html", "r", encoding="utf-8") as f:
    html_content = f.read()

msg = MIMEMultipart("alternative")
msg["From"] = SENDER
msg["To"] = ", ".join(RECIPIENTS)
msg["Subject"] = subject

plain_text = "Desítka Newsletter."
msg.attach(MIMEText(plain_text, "plain", "utf-8"))
msg.attach(MIMEText(html_content, "html", "utf-8"))

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER, APP_PASSWORD)
    server.sendmail(SENDER, RECIPIENTS, msg.as_string())

print(f"E-mail odeslán na: {', '.join(RECIPIENTS)}")
