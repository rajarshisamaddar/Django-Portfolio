from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import Contact


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


@csrf_exempt
def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        subject = request.POST['subject']
        messageR = request.POST['message']

        contact = Contact(name=name, email=email,
                          phone=phoneNumber, subject=subject, message=messageR)
        contact.save()

        messagedict = {
            "Name": name,
            "Email": email,
            "Phone Number": phoneNumber,
            "Subject": subject,
            "Message": messageR
        }

        mail_content = str(messagedict)
        sender_address = 'ignorecrowdweb@gmail.com'
        sender_pass = 'secure@Rajpas1'
        receiver_address = 'ignorecrowd@gmail.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        # The subject line
        message['Subject'] = "A message recieved on Django"
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail

        message2 = MIMEMultipart()
        message2['From'] = sender_address
        message2['To'] = email
        # The subject line
        message2['Subject'] = "Message Received"
        # The body and the attachments for the mail
        message2.attach(MIMEText(
            "Thank you for your message. This is a system-generated email you are receiving please do not reply here I will contact you ASAP. I appreciate your interest. Thank you again.", 'plain'))
        # Create SMTP session for sending the mail

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        # login with mail_id and password
        session.login(sender_address, sender_pass)
        text = message.as_string()
        text2 = message2.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.sendmail(sender_address, email, text2)
        session.quit()
    return redirect('/contact')
