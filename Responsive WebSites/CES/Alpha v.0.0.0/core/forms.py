from django import forms
from django.core.mail.message import EmailMessage
from django.db.models import fields


from .models import Noticia


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
            from_email = 'youremail',
            to = ['youremail'],
            headers = {'Replay To': email},
        )

        mail.send()

class NewsModelForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['nome','descricao', 'texto','imagem','imagem_2','imagem_3','imagem_4']


## CUSTOMUSER

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUsuario

class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone','cpf','funcao','identificacao')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone','cpf','funcao','identificacao')
        