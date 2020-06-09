from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject_email = forms.CharField(label='Matter', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject_email = self.cleaned_data['subject_email']
        message = self.cleaned_data['message']

        content = f'Name:{name}\nE-mail:{email}\nSubject:{subject_email}\nMessage:{message}'
        mail = EmailMessage(
            subject=subject_email,
            body=content,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br', ],
            headers={'Reply-To': email}
        )
        mail.send()
