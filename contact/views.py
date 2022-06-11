from tabnanny import check
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .models import Contact, ContactFindMe, ContactParagraph
import random

check = 0
operation = ""
number_one = 0
number_two = 0


def error(request):
    template = loader.get_template('error_page.html')
    return HttpResponse(template.render())


def contact(request):
    contactparagraph = ContactParagraph.objects.all().values()
    contactfindme = ContactFindMe.objects.all().values()
    op_type = round(random.random())
    number_one = random.randint(51, 99)
    number_two = random.randint(1, 50)
    global check
    if(op_type == 0):
        operation = "-"
        check = number_one - number_two
    else:
        operation = "+"
        check = number_one + number_two
    context = {
        'contactparagraph': contactparagraph,
        'contactfindme': contactfindme,
        'number_one': number_one,
        'number_two': number_two,
        'operation': operation,
    }
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))


@csrf_exempt
def message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneNumber = request.POST['phoneNumber']
        subject = request.POST['subject']
        messageR = request.POST['message']
        messageR = request.POST['message']
        captcha = request.POST['captcha']
        if(int(captcha) == check):
            contact = Contact(
                name=name, email=email, phone=phoneNumber, subject=subject, message=messageR)
            contact.save()

            # messagedict = "Name: "+name+"\r\r\n Email: "+email + "\r\r\n Phone Number: " + \
            #     phoneNumber+"\r\r\n Subject: "+subject+"\r\r\n Message: "+messageR

            # mail_content = str(messagedict)
            # sender_address = 'ignorecrowdweb@gmail.com'
            # sender_pass = 'secure@Rajpas1'
            # receiver_address = 'ignorecrowd@gmail.com'
            # # Setup the MIME
            # message = MIMEMultipart()
            # message['From'] = sender_address
            # message['To'] = receiver_address
            # # The subject line
            # message['Subject'] = "A message recieved on ignorecrowd.co.in"
            # # The body and the attachments for the mail
            # message.attach(MIMEText(mail_content, 'plain'))
            # # Create SMTP session for sending the mail

            # message2 = MIMEMultipart()
            # message2['From'] = sender_address
            # message2['To'] = email
            # # The subject line
            # message2['Subject'] = "Thank you " + \
            #     name + " for your immediate response."

            # mail_content2 = "Dear "+name+",\r\r\n If you receive an email response immediately after sending your message, it's very likely an auto-response confirmation message. I suggest waiting until you get a reply that was not automatically generated before you reply. \r\r\n I will review your message and will be in touch with you soon to move forward with our conversation. \r\r\n Regards, \r\r\n Rajarshi Samaddar \r\r\n ignorecrowd.co.in"
            # # The body and the attachments for the mail
            # message2.attach(MIMEText(mail_content2, 'plain'))
            # # Create SMTP session for sending the mail

            # # use gmail with port
            # session = smtplib.SMTP('smtp.gmail.com', 587)
            # session.starttls()  # enable security
            # # login with mail_id and password
            # session.login(sender_address, sender_pass)
            # text = message.as_string()
            # text2 = message2.as_string()
            # session.sendmail(sender_address, receiver_address, text)
            # session.sendmail(sender_address, email, text2)
            # session.quit()
            return redirect('/contact/')
        else:
            return redirect('error')

    # return redirect('/contact')
