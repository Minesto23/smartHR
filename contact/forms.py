from django import forms
from .models import Quote, Model_Quote, Turns

class ContactForm(forms.Form):
    name = forms.CharField(label="*Your Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'*Your Name'}
    ))
    lastname = forms.CharField(label="*Your LastName", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'*Your LastName'}
    ))
    email = forms.EmailField(label="*Email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'*Your Email'}
    ))
    subject = forms.CharField(label="*Subject",required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'*Subject'}
    ))
    content = forms.CharField(label="*Message", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'*Message'}
    ))

class DateInput(forms.DateInput):
    input_type = 'date'



class QuoteForm(forms.ModelForm):
    name = forms.CharField(label="*Your Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes', 'placeholder':'*For Example:Kat'}
    ))
    lastname = forms.CharField(label="Your LastName", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes', 'placeholder':'*For Example:Jones'}
    ))
    email = forms.EmailField(label="*Email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes', 'placeholder':'*For Example:katJ@email.com'}
    ))
    phone_number = forms.CharField(label="*Your Cellphone",required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes', 'placeholder':'*For Example:123-0000-000'}
    ))
    date = forms.DateField(label="*Date",required=True, widget=DateInput)
    turn = forms.CharField(label="*Turn",required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes', 'placeholder':'*Your Name'}
    ))

    class Meta:
        model = Quote
        fields = ['name','lastname','email','phone_number','date','turn']


                


    
            
