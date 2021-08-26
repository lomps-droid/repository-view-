from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','texto','imagem','imagem_2','imagem_3','imagem_4','slug', 'criado', 'modificado', 'ativo')


from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone','cpf','funcao','identificacao')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


from .models import AlunoCadastro, Turma, Porturgue, Matematic, Geografia, Historia, Biologia, Fisica, Quimica

@admin.register(AlunoCadastro)
class AddAluno(admin.ModelAdmin):
    list_display = ('nome','matricula','nascimento')

@admin.register(Turma)
class AddTurmas(admin.ModelAdmin):
    list_display = ('nome_da_turma',)

#MATÉRIAS
@admin.register(Porturgue, Matematic, Geografia, Historia, Biologia, Fisica, Quimica)
class AddMateriaPort(admin.ModelAdmin):
    list_display = ('matricula','media')



