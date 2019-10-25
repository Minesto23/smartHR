from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    subject = forms.CharField(label="Subject",required=True)
    email = forms.EmailField(label="Email", required=True)
    content = forms.CharField(label="Content", required=True, widget=forms.Textarea)