from django.shortcuts import render

from django import forms
from .forms import ContatoFrom
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoFrom(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()


            messages.success(request, 'Email enviado com sucesso!')
            form = ContatoFrom()
        else:
            messages.error(request, 'Erro ao enviar email!')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def update_page(request):
    return render(request, 'updates.html')