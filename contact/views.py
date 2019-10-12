from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject','')
            content = request.POST.get('content', '')

            # Creamos el correo
            email = EmailMessage(
                "Smart HR: New Message ({})".format(subject),
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                from_email='no-contestar@inbox.mailtrap.io',
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})