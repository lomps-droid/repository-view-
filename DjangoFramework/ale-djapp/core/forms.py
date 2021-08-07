from django import forms
from django.core.mail.message import EmailMessage


class ContatoFrom(forms.Form):
    nome = forms.CharField(label='Nome', max_length=120)
    assunto = forms.CharField(label='Assunto', max_length=120)
    email = forms.EmailField(label='E-mail', max_length=120)
    texto = forms.CharField(label='Texto', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        assunto = self.cleaned_data['assunto']
        email = self.cleaned_data['email']
        texto = self.cleaned_data['texto']

        conteudo = f'Nome: {nome}\nEnviado por: {email}\nAssunto: {assunto}\nMensagem: {texto}'

        mail = EmailMessage(
            subject = 'Email enviado pelo sistema',
            body = conteudo,
            from_email = 'your email',
            to = ['your email'],
            headers = {'Replay To': email},
        )

        mail.send()


