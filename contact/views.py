import datetime
import time
from django.shortcuts import render, redirect
from .forms import ContactForm, QuoteForm
from .models import Quote, Turns, Model_Quote
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings

def contact(request):
      contact_form = ContactForm()
      quote_form = QuoteForm()
      print('hecho')
      val = 0
      if request.method=='POST':
            if request.POST.get('button') == 'quote':
                  quote_form = QuoteForm(request.POST)
                  quote_comp = Quote.objects.all()
                  quote_number = Quote.objects.all().count()
                  date_comp = str_to_date(request.POST['date'])
                  turn_comp = request.POST['turn']
                  print("turn:"+turn_comp)
                  print("date:"+str(date_comp))
                  print("numero registros:"+str(quote_number))
                  print('Abriendo Guardado')
                  # quote_compare = 
                  if quote_number == 0:
                        if quote_form.is_valid():
                              print('Guardando')
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
                                          print('no es igual')
                                          val = 0
                                    elif date_comp == quote.date and turn_comp == quote.turn:
                                          print(str(quote.date))
                                          print(str(quote.turn))
                                          print('es igual')
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
                              print('Guardando')
                              quote = quote_form.save()
                              quote.turn = request.POST['turn']
                              quote.save()  
                              #enviamos correo
                              name = request.POST.get('name', '')
                              lastname = request.POST.get('lastname','')
                              email = request.POST.get('email', '')
                              phone_number = request.POST.get('phone_number','')
                              date = request.POST.get('date', '')
                              turn = request.POST.get('turn', '')

                              # Creamos el correo
                              email = EmailMessage(
                              "SmartHR: New Quote",
                              "From {} <{}>\n\nPhone number:{}\n\nDate:{}\n\nTurn:{}".format(name, email,phone_number,date,turn),
                              "it@smarthrfl.com",
                              to=['minesto23@gmail.com','Info@smarthrfl.com'],
                              reply_to=[email]
                              )
                              # Lo enviamos y redireccionamos
                              try:
                                    email.send()
                                    return redirect(reverse('contact')+"?ok_q")
                              except:
                                    # Algo no ha ido bien, redireccionamos a FAIL
                                    return redirect(reverse('contact')+"?fail")


            elif request.POST.get('button') == 'email':
                  contact_form = ContactForm(data=request.POST)
                  if contact_form.is_valid():
                              name = request.POST.get('name', '')
                              lastname = request.POST.get('lastname','')
                              email = request.POST.get('email', '')
                              subject = request.POST.get('subject','')
                              content = request.POST.get('content', '')

                              # Creamos el correo
                              email = EmailMessage(
                              "SmartHR: New Message ({})".format(subject),
                              "De {} <{}>\n\nWrite:\n\n{}".format(name, email, content),
                              "it@smarthrfl.com",
                              to=['minesto23@gmail.com','Info@smarthrfl.com'],
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