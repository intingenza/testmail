import os
import sendgrid
from sendgrid.helpers.mail import *

# Build mail
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

from_email = Email(os.environ.get("SENDER"))

to_email = Email(os.environ.get("RECEIVER"))

email = Mail()

email.from_email = from_email
email.subject = 'Made it to send email'

personalization = Personalization()
personalization.add_to(to_email)

email.add_personalization(personalization)

cnt = Content('text/plain', '-')
email.add_content(cnt)

# Send mail
try:
    response = sg.send(email.get())
except Exception as e:
    raise e

