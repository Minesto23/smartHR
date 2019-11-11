from django import forms
from .models import Quote, Model_Quote, Turns

CHOICES=(
    ('1-10','1-10'),
    ('11-50','11-50'),
    ('51-200','51-200'),
    ('+200','+200'),
)

class ContactForm(forms.Form):
    company_name = forms.CharField(label="Company Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control' }
    ))
    contact_name = forms.CharField(label="Contact Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(label="Email*", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    phone_number = forms.CharField(label="Phone Number",required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    number_employees= forms.ChoiceField(label="Number of Employees" ,choices=CHOICES, required=True, widget=forms.Select(
        attrs={'class':'form-control'}
    ))
    content = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3}
    ))

class DateInput(forms.DateInput):
    input_type = 'date'



class QuoteForm(forms.ModelForm):
    name = forms.CharField(label="*Your Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes'}
    ))
    lastname = forms.CharField(label="Your LastName", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes'}
    ))
    email = forms.EmailField(label="*Email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes'}
    ))
    phone_number = forms.CharField(label="*Your Cellphone",required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes'}
    ))
    date = forms.DateField(label="*Date",required=True, widget=DateInput)
    turn = forms.CharField(label="*Turn",required=True, widget=forms.TextInput(
        attrs={'class':'form-control quotes'}
    ))

    class Meta:
        model = Quote
        fields = ['name','lastname','email','phone_number','date','turn']


                


    
            
