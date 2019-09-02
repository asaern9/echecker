from django import forms
from . models import Contact, Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'name': 'name', 'placeholder': 'Enter your name', 'type': 'text'}),
            'email': forms.TextInput(attrs={'class': 'form-control', "type": "email", "id": "email", "name": "email", "placeholder": "Enter email address"}),
            'subject': forms.TextInput(attrs={"type": "text", "class": "form-control", "id": "subject", "name": "subject", "placeholder":"Enter Subject"}),
            'message': forms.Textarea(attrs={"class": "form-control", "id": "message", 'rows': 1,  "name": "message", "placeholder":"Enter Message"})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"type": "text", "class": "form-control", "id": "name", "placeholder": "Enter Name",
                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Name'"}),
            'phone': forms.TextInput(attrs={"type": "text", "class": "form-control", "id": "phone", "placeholder": "Enter Phone",
                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Phone'"}),
            'reference': forms.TextInput(attrs={"type": "text", "class": "form-control", "id": "ref", "placeholder": "Enter Reference(optional)",
                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Reference(optional)'"}),
            'comment': forms.Textarea(attrs={"type": "text", "class": "form-control mb-10", "rows": 5, "id": "comment", "placeholder": "Enter Comment(optional)",
                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Comment(optional)'"}),
            'checker': forms.Select(attrs={"type": "text", "class": "form-control", "id": "name",
                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Name'"}),
        }