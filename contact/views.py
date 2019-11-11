import datetime
import os
import time
from django.shortcuts import render, redirect
from .forms import ContactForm, QuoteForm
from .models import Quote, Turns, Model_Quote
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from email.mime.image import MIMEImage
from django.conf import settings

def contact(request):
      contact_form = ContactForm()
      quote_form = QuoteForm()
      # print('hecho')
      val = 0
      if request.method=='POST':
            if request.POST.get('button') == 'quote':
                  quote_form = QuoteForm(request.POST)
                  quote_comp = Quote.objects.all()
                  quote_number = Quote.objects.all().count()
                  date_comp = str_to_date(request.POST['date'])
                  turn_comp = request.POST['turn']
                  # print("turn:"+turn_comp)
                  # print("date:"+str(date_comp))
                  # print("numero registros:"+str(quote_number))
                  # print('Abriendo Guardado')
                  # quote_compare = 
                  if quote_number == 0:
                        if quote_form.is_valid():
                              # print('Guardando')
                              quote_n = quote_form.save()
                              quote_n.turn = request.POST['turn']
                              quote_n.save()      
                              return redirect(reverse('contact')+"?ok_q")
                        else:
                              quote_form = QuoteForm()
                  else:
                        for quote in quote_comp:
                              if quote_form.is_valid():
                                    if date_comp != quote.date and turn_comp != quote.turn:
                                          # print('no es igual')
                                          val = 0
                                    elif date_comp == quote.date and turn_comp == quote.turn:
                                          # print(str(quote.date))
                                          # print(str(quote.turn))
                                          # print('es igual')
                                          val = 1
                                          break
                              else:
                                    quote_form = QuoteForm()
                                    val = -1
                                    return redirect(reverse('contact')+"?not_q")
                                    break 
                        if val == 1:
                              quote_form = QuoteForm()
                              return redirect(reverse('contact')+"?same_q")
                        elif val == 0:
                              # print('Guardando')
                              quote = quote_form.save()
                              quote.turn = request.POST['turn']
                              quote.save()  
                              #enviamos correo
                              name = request.POST.get('name', '')
                              lastname = request.POST.get('lastname','')
                              emailc = request.POST.get('email', '')
                              phone_number = request.POST.get('phone_number','')
                              date = request.POST.get('date', '')
                              turn = request.POST.get('turn', '')
                              template = get_template('email_quotes.html')
                              template2 = get_template('email_quotes2.html')

                              message = template.render({'name':name , 'lastname':lastname, 'email':emailc,'date':date,'turn':turn})
                              message2 = template2.render({'name':name , 'lastname':lastname, 'email':emailc, 'phone_number':phone_number,'date':date,'turn':turn})


                              # Creamos el correo
                              email = EmailMessage(
                              "SmartHR: Confirmation Quote",
                              message,
                              "it@smarthrfl.com",
                              to=[emailc],
                              )
                              email2 = EmailMessage(
                              "SmartHR: New Quote",
                              message2,
                              "it@smarthrfl.com",
                              to=['Info@smarthrfl.com'],
                              reply_to=[emailc]
                              )
                              # Lo enviamos y redireccionamos
                              try:
                                    email.send()
                                    email2.send()
                                    return redirect(reverse('contact')+"?ok_q")
                              except:
                                    # Algo no ha ido bien, redireccionamos a FAIL
                                    return redirect(reverse('contact')+"?fail")


            elif request.POST.get('button') == 'email':
                  contact_form = ContactForm(data=request.POST)
                  if contact_form.is_valid():
                              company_name = request.POST.get('company_name', '')
                              contact_name = request.POST.get('contact_name','')
                              email = request.POST.get('email', '')
                              number_employees = request.POST.get('number_employees','')
                              content = request.POST.get('content', '')
                              template = get_template('email.html')
                              
                              # context = Context({'name':name})
                              message = template.render({'name':name , 'company_name':company_name, 'email':email, 'number_of_employees':number_employees, 'content':content})

                              # Creamos el correo
                              email = EmailMessage(
                              "SmartHR: New Message ({})".format(company_name),
                              # "De {} <{}>\n\nWrite:\n\n{}".format(name, email, content),
                              message,
                              "it@smarthrfl.com",
                              to=['it@smarthrfl.com'],
                              # 'Info@smarthrfl.com'
                              reply_to=[email]
                              )
                              email.content_subtype = 'html'

                              for f in ['Horizontal-Positivo@2x.png']:
                                    fp = open(os.path.join(os.path.dirname(__file__), f), 'rb')
                                    email_img = MIMEImage(fp.read())
                                    fp.close()
                                    email_img.add_header('Content-ID', '<{}>'.format(f))
                                    email.attach(email_img)

                              # Lo enviamos y redireccionamos
                              try:
                                    email.send()
                                    # Todo ha ido bien, redireccionamos a OK
                                    return redirect(reverse('contact')+"?ok")
                              except:
                                    # Algo no ha ido bien, redireccionamos a FAIL
                                    return redirect(reverse('contact')+"?fail")
      return render(request,"contact/contact.html",{'form_quote':quote_form,'form_email':contact_form})


def Load_Turns(request):
      date_cap = str_to_weekday(request.GET.get('date'))
      date_u = date_cap
      date_model = Model_Quote.objects.filter(day_code=date_u).order_by('created')
      return render(request, 'contact/load_turns.html', {'date': date_model})

def to_djangoweekday(date):
   return date.weekday()

def str_to_weekday(date):
      date_object = datetime.datetime.strptime(date, "%Y-%m-%d").date()
      date_object = date_object.weekday()
      return date_object

def str_to_date(date):
      date_object = datetime.datetime.strptime(date, "%Y-%m-%d").date()
      return date_object