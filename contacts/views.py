from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Отправка email
            send_mail(
                f'Сообщение от {name}: {subject}',
                f'От: {email}\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return render(request, 'contacts/success.html')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contacts/contact.html', context) 