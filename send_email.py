import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER = "szczjr@gmail.com"
APP_PASSWORD = "muzk jdcx qsqz maix"
RECIPIENT = "aneta.hoschlova@gmail.com"
SUBJECT = "Praha 10 Newsletter | 20. dubna – 4. května 2026"

with open("digest.html", "r", encoding="utf-8") as f:
    html_content = f.read()

msg = MIMEMultipart("alternative")
msg["From"] = SENDER
msg["To"] = RECIPIENT
msg["Subject"] = SUBJECT

plain_text = "Newsletter Praha 10 – pro zobrazení použijte HTML verzi tohoto e-mailu."
msg.attach(MIMEText(plain_text, "plain", "utf-8"))
msg.attach(MIMEText(html_content, "html", "utf-8"))

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(SENDER, APP_PASSWORD)
    server.sendmail(SENDER, RECIPIENT, msg.as_string())

print("E-mail odeslán.")
