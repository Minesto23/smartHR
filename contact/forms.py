from django import forms
from .models import Quote, Model_Quote, Turns

class ContactForm(forms.Form):
    name = forms.CharField(label="*Your Name", required=True, widget=forms.TextInput(
        attrs={'class':'form-control' }
    ))
    lastname = forms.CharField(label="*Your LastName", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    email = forms.EmailField(label="*Email", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    subject = forms.CharField(label="*Subject",required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    content = forms.CharField(label="*Message", required=True, widget=forms.Textarea(
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


                


    
            
