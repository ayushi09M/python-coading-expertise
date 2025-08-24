import smtplib
import logging
import re
import dns.resolver
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------- Logging Setup ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- Validation Functions ----------------
def is_valid_email_format(email: str) -> bool:
    """Check if email format is correct."""
    pattern = r"^[\w\.-]+@([\w\.-]+)\.\w+$"
    return re.match(pattern, email) is not None

def has_mx_record(domain: str) -> bool:
    """Check if domain has MX records."""
    try:
        dns.resolver.resolve(domain, "MX")
        return True
    except Exception:
        return False

def validate_email(email: str) -> bool:
    """Validate email format and domain with logging."""
    logging.info(f"Validating email '{email}'...")
    if not is_valid_email_format(email):
        logging.error(f"❌ Invalid email format: {email}")
        return False

    domain = email.split("@")[1]
    if not has_mx_record(domain):
        logging.error(f"❌ Domain '{domain}' does not have mail servers")
        return False

    logging.info(f"✅ Email '{email}' looks valid")
    return True

# ---------------- Config ----------------
sender_email = "microverse.platform@gmail.com"
password = "gcyr zxkp peqx hfco"

# List of recipients
to_emails = ["ayushi99malviya@gmail.com", "ayushi200malviya@gmail.com"]       # main recipients
cc_emails = ["ayushi09malviya@gmail.com"]                            # CC recipients
bcc_emails = ["bookish.glimpse@gmail.com"]                           # BCC recipients

# ---------------- Step 1: Validate Sender & Recipients ----------------
if not validate_email(sender_email):
    raise ValueError("Sender email is invalid!")

all_recipients = to_emails + cc_emails + bcc_emails
valid_recipients = []
for email in all_recipients:
    if validate_email(email):
        valid_recipients.append(email)

if not valid_recipients:
    raise ValueError("No valid recipient emails!")

# ---------------- Step 2: Create Email ----------------
logging.info("Creating email message...")
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = ", ".join(to_emails)
msg["CC"] = ", ".join(cc_emails)
msg["Subject"] = "Hello from Python - Multiple Recipients 🚀"

body = "Hi everyone! This is a test email sent by Python to multiple recipients. 🐍✨"
msg.attach(MIMEText(body, "plain"))

# ---------------- Step 3: Send Email ----------------
try:
    logging.info("Connecting to Gmail SMTP server...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        logging.info("Starting TLS encryption...")
        server.starttls()

        logging.info(f"Logging in as '{sender_email}'...")
        server.login(sender_email, password)

        # Send email to all valid recipients
        logging.info("Sending email to all recipients...")
        server.sendmail(sender_email, valid_recipients, msg.as_string())
        logging.info(f"✅ Email sent successfully to: {', '.join(valid_recipients)}")

except smtplib.SMTPAuthenticationError as e:
    logging.error("❌ Authentication failed. Did you use an App Password?")
    logging.exception(e)
except Exception as e:
    logging.error("❌ An error occurred while sending email")
    logging.exception(e)
