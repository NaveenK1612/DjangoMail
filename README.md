# DjangoMail
Hackathon Project to send emails from Django +celery


### Trigger email from local. 
Make sure you have following environment variables


export EMAIL_HOST="abc.x"
export EMAIL_PORT=587
export EMAIL_HOST_USER="abc@abc.com"
export EMAIL_HOST_PASSWORD="abc"
export EMAIL_USE_TLS=True
export DEFAULT_FROM_EMAIL="abc@abc.com"

Go to Django Shell and call the utill

from mail.utils import *
send_welcome_email("youremail.abc.com", "your name")

