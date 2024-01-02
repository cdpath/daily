from datetime import datetime
import smtplib
import os
from email.message import EmailMessage


current_date_str = datetime.now().strftime("%Y%m%d")

email_user = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASSWORD')
kindle_email = os.environ.get('KINDLE_EMAIL')


msg = EmailMessage()
msg['Subject'] = 'LeetCode Question'
msg['From'] = email_user
msg['To'] = kindle_email
msg.set_content('Please find the attached LeetCode question.')


file_path = 'LeetCode_Question.pdf'
with open(file_path, 'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=f'LeetCode_Question_{current_date_str}.pdf')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_user, email_password)
    smtp.send_message(msg)

