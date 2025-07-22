# Code #88: Send an Email Using Python (SMTP)
"""
    🧠 Why This Matters?
    Used in:
    - 📧 Auto-notifications from scripts or apps
    - 🧾 Sending logs or backup confirmations
    - 🌤️ Mailing weather or currency reports
    - 📦 Order confirmations and user alert
"""
# Tier: Intermediate
# Goal: Use the built-in smtplib module to send an email with subject and body

# Python Code (Using Gmail SMTP)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, password, receiver, subject, body):
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()  # Secure connection

            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print("✅ Email sent successfully.")
    except:
        print("❌ Failed to send email:", e)

# Sample Usage

send_email(
    sender = "your_sender_email",
    password = "your_app_password", # you can visit https://www.youtube.com/watch?v=hXiPshHn9Pw to create your own password

    receiver="your_reciever_email",
    subject="Daily Weather Report",
    body="Today's temperature in Bengaluru is 25°C With light rain. "
)

# Gmail Security Note
"""
    🔐 Gmail Security Note
    - Create an App Password from your Google Account → Security → App Passwords
    - You’ll need to enable 2FA (two-factor authentication) to use App Passwords
    - Avoid using your actual Gmail password directly
"""

# Concept Breakdown
"""
    Concept         Description
    ---------------------------
    smtplib         Python's built-in SMTP client
    starttls()      Encrypts your email transaction
    MIMEText        Allows rich formatting (plain/text/HTML)
    sendmail()      Sends the constructed message
"""
# You can attach files, send HTML newsletters, or triggeremails from automation scripts.

# Real-World Connection
"""
    - Deliver weather, currency, or to-do updates
    - Notify admins of script failures or system alerts
    - Email receipts, invoices, or confirmation messages
    - Hook into chatbot or CLI reporting
"""
