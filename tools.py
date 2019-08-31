from django.core.mail import send_mass_mail

from .models import Contact

def send_email(contacts: [str], text: str) -> None:
    emails = []
    for contact in contacts:
        emails.append((
            'Reminder for ' + text,
            'Hello ' + str(Contact.objects.get(id=contact)) + ',' + '\n\n\n\n' +
            'This is a reminder for ' + text + '.' + '\n\n\n\n' + "From MyTodo Team",
            'fromemail@email.com',
            [Contact.objects.get(id=contact).get_email()]
        ))
    send_mass_mail(tuple(emails), fail_silently=False)