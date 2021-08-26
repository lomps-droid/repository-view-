from django.contrib.auth.models import User
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .models import Noticia, AlunoCadastro
from .forms import ContatoFrom, NewsModelForm
from django.contrib import messages


#CRUD
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news'] = Noticia.objects.order_by("-id") #Noticia.objects.all()
        context['user_type'] = str(self.request.user.is_staff)
        #teste = AlunoCadastro.objects.get(matricula=self.request.user.identificacao)
        #print(teste)
        #print(teste.disciplina_1.nota01)
        return context



class ContatoView(TemplateView):
    template_name = 'contato.html'
    form_class = ContatoFrom
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        context['user_type'] = str(self.request.user.is_staff)
        return context


    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(ContatoView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail, tente novamente.')
        return super(ContatoView, self).form_invalid(form, *args, **kwargs)



class NewsView(FormView):
    template_name = 'news.html'
    form_class = NewsModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['user_type'] = str(self.request.user.is_staff)
        return context
    

    def form_valid(self, form, *args, **kwargs):
        #form = NewsModelForm(self.request.POST, self.request.FILES)
        form.save()
        messages.success(self.request, 'Notícia postada com sucesso')
        return super(NewsView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar Notícia para o sistema')
        return super(NewsView, self).form_invalid(form, *args, **kwargs)


class NoticiasView(TemplateView):
    template_name = 'noticias.html'
    
    def get_context_data(self, slug_id, **kwargs):
        context = super(NoticiasView, self).get_context_data(**kwargs)
        context['news'] = Noticia.objects.get(slug=slug_id)
        context['user_type'] = str(self.request.user.is_staff)
        return context


#CRUD
class ListNoticiaView(ListView):
    model = Noticia
    template_name = 'notlist.html'
    queryset = Noticia.objects.all()
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = str(self.request.user.is_staff)
        return context

class UpdateNoticiaView(UpdateView):
    model = Noticia
    template_name = 'update_form.html'
    fields = ['nome', 'descricao','texto','imagem','imagem_2','imagem_3','imagem_4']
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = str(self.request.user.is_staff)
        return context

class DeleteNoticiaView(DeleteView):
    model = Noticia
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = str(self.request.user.is_staff)
        return context
######

class EventosView(TemplateView):
    template_name = 'eventos.html'
    
    def get_context_data(self, **kwargs):
        context = super(EventosView, self).get_context_data(**kwargs)
        context['news'] = Noticia.objects.order_by("-id")
        context['user_type'] = str(self.request.user.is_staff)
        return context

class AlunoAreaView(TemplateView):
    template_name = 'estudante.html'

    def get_context_data(self,slug_id, **kwargs):
        context = super(AlunoAreaView, self).get_context_data(**kwargs)
        get_aluno = AlunoCadastro.objects.get(matricula=self.request.user.identificacao)
        #print(teste)
        #print(teste.disciplina_1.nota01)
        context['aluno_verify'] = str(slug_id)
        context['aluno_confirm'] =str(self.request.user.identificacao)
        context['aluno'] = AlunoCadastro.objects.get(matricula=get_aluno)
        context['user_type'] = str(self.request.user.is_staff)
        return context