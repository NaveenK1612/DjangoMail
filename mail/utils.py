import smtplib

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(subject: str, text_content: str, to: str, html_content: str = None):
    """
    task to send email according to the given params.
    """
    msg = EmailMultiAlternatives(
        subject=subject, body=text_content, to=to, from_email=settings.DEFAULT_FROM_EMAIL
    )
    if html_content:
        msg.attach_alternative(html_content, "text/html")
    try:
        return_data = msg.send()
    except smtplib.SMTPException as e:
        print('[SendEmailTask] Email failed')
        return_data = 0
    else:
        print('[SendEmailTask] Email sent')
    return return_data


def render_and_send_email(
        subject_template_name: str, body_template_name: str, to: list, subject_context: dict = None,
        body_context: dict = None, **kwargs):
    """
    Renders body-template using given context, and sends the email accordingly.
    """
    subject = render_to_string(u'{}.txt'.format(subject_template_name), subject_context or {})
    email_body_text = render_to_string(u'{}.txt'.format(body_template_name), body_context or {})
    email_body_html = render_to_string(u'{}.html'.format(body_template_name), body_context or {})
    return send_email(
        subject=subject, text_content=email_body_text, to=to, html_content=email_body_html,
        **kwargs
    )


def send_welcome_email(to: str = settings.DEFAULT_FROM_EMAIL, user_name: str = "Django User"):
    """
    Driver function to send email to a particular email address and user name. 
    :param to:
    :param user_name:
    :return:
    """
    render_and_send_email(
        subject_template_name='mail/welcome/subject',
        body_template_name='mail/welcome/body',
        to=[to],
        body_context={
            'user_name': user_name
        },
        subject_context={'user_name': user_name},
    )
