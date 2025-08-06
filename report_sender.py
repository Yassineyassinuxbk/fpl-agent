import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_report(current_team, transfers):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    body = f"[FPL Agent Report – {now}]\n\n"
    body += "Transfers made:\n"
    for t in transfers:
        body += f" OUT: {t['out']} → IN: {t['in']}\n"
    body += "\nCurrent team (simplified):\n"
    for player in current_team:
        body += f" - {player['element']} | Pts: {player['points']}\n"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = f"FPL Agent Report – {now}"
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_FROM, EMAIL_APP_PASSWORD)
            smtp.send_message(msg)
        print("[Email] Report sent successfully.")
    except Exception as e:
        print(f"[Email] Failed to send report: {e}")
