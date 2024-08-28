from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class EmailService:
    @staticmethod
    def send_email_with_attachment(subject, message, recipient_list, attachment_path, from_email=None):
        """
        Envia um email com anexo, opcionalmente pode incluir corpo HTML.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )

        email.attach_file(attachment_path)  # Anexa o arquivo

        email.send()