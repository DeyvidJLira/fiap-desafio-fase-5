import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import base64

from constants import DISABLE_EMAIL_SERVICE

# Esta função utiliza a biblioteca SendGrid para enviar e-mail com anexo.
def send_email(subject, body, attachment_content=None, attachment_name=None, attachment_type='image/jpg'):
    if DISABLE_EMAIL_SERVICE:
        print("Serviço de e-mail desativado.")
        return

    sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
    
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=os.getenv("TO_EMAIL"),
        subject=subject,
        plain_text_content=body
    )
    
    if attachment_content and attachment_name:
        encoded_content = base64.b64encode(attachment_content).decode()
        attachment = Attachment(
            FileContent(encoded_content),
            FileName(attachment_name),
            FileType(attachment_type),
            Disposition('attachment')
        )
        message.attachment = attachment

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"E-mail enviado! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")