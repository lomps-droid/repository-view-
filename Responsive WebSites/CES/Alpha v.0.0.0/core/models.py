from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.forms import widgets
from stdimage.models import StdImageField

#For AbstractUser - CustomUser

# Create your models here.

from django.db.models import signals #Antes de inserir os dados nos bancos ele faz algo antes com esses dados
from django.template.defaultfilters import slugify #Ele pega o título do 'produto' e cria uma url

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Noticia(Base):
    nome = models.CharField('Titulo da Noticia', max_length=100)
    descricao = models.TextField('Descrição', max_length=1000, help_text='Máximo de 1000 caracteres')
    texto = models.TextField('Parágrafo 01')
    #preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to='news')
    imagem_2 = StdImageField('Galeria 01', upload_to='news',blank=True, default=None)
    imagem_3 = StdImageField('Galeria 02', upload_to='news',blank=True, default=None)
    imagem_4 = StdImageField('Galeria 03', upload_to='news',blank=True, default=None)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    
    def __str__(self) -> str:
        return self.nome
    

def noticia_pre_save(signal, instance, sender, **kwargs): #Antes de salvar no banco de dados vai rodar isso
    instance.slug = slugify(instance.nome) #Ele pega o nome do Noticia e transforma para maria-mole para poder transformar isso em URL

signals.pre_save.connect(noticia_pre_save, sender=Noticia) #Quando esse cara "Noticia" for salvo, ele vai executar a função


#CREATE USERCUSTOM

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15, blank=True, default='Não possui')
    cpf = models.CharField('CPF', max_length=11)
    funcao = models.CharField('Função', max_length=20, blank=True, default='Não possui')
    identificacao = models.CharField('Identificação', max_length=20, unique=True)

    is_staff = models.BooleanField('Membro da equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone','cpf','funcao','identificacao']

    def __str__(self):
        return self.email

    objects = UsuarioManager()


#END CREATE USERCUSTOM

#TURMAS
class Turma(Base):
    nome_da_turma = models.CharField('Turma', max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nome_da_turma

#MATÉRIAS

class Porturgue(Base):
    nome = models.CharField('Matéria', max_length=100, blank=True, default='Ex: Português')
    matricula = models.CharField('Confirmar Matrícula', max_length=100) #Mesma 'Identificação' do Usuário
    nota01 = models.DecimalField('Nota 01', max_digits=5, decimal_places=1,blank=True, default=0)
    nota02 = models.DecimalField('Nota 02', max_digits=5, decimal_places=1,blank=True, default=0)
    nota03 = models.DecimalField('Nota 03', max_digits=5, decimal_places=1,blank=True, default=0)
    nota04 = models.DecimalField('Nota 04', max_digits=5, decimal_places=1,blank=True, default=0)
    nota05 = models.DecimalField('Nota 05', max_digits=5, decimal_places=1,blank=True, default=0)
    nota06 = models.DecimalField('Nota 06', max_digits=5, decimal_places=1,blank=True, default=0)
    media = models.DecimalField('Média', max_digits=5, decimal_places=1,blank=True, default=0)
    faltas = models.CharField('Número de Faltas',max_length=100,blank = True, default='0')
    status = models.CharField('Situação do Aluno',max_length=100,blank = True, default="Em Progresso")
    observacao = models.TextField('Observação do Professor',blank = True, default="Nenhuma observação adicionada")
    
    def __str__(self) -> str:
        return self.matricula

class Matematic(Porturgue):
    pass

class Geografia(Porturgue):
    pass

class Historia(Porturgue):
    pass

class Biologia(Porturgue):
    pass

class Fisica(Porturgue):
    pass

class Quimica(Porturgue):
    pass


#ALUNO CADASTRO

class AlunoCadastro(Base): #ID do Primeiro Ano: 1
    nome = models.CharField('Nome do Aluno', max_length=100)
    matricula = models.CharField('Matrícula', max_length=100, unique=True) #Mesma 'Identificação' do Usuário
    dados = models.OneToOneField(CustomUsuario, on_delete=models.CASCADE, null=True, unique=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    nascimento = models.CharField('Data de Nascimento', max_length=15, default='XX/XX/XXXX')
    ## /////////////////////////////////////////////////////////
    disciplina_1 = models.OneToOneField(Porturgue, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina01', help_text='Português')
    disciplina_2 = models.OneToOneField(Matematic, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina02', help_text='Matemática')
    disciplina_3 = models.OneToOneField(Geografia, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina03', help_text='Geografia')
    disciplina_4 = models.OneToOneField(Historia, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina04', help_text='História')
    disciplina_5 = models.OneToOneField(Biologia, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina05', help_text='Biologia')
    disciplina_6 = models.OneToOneField(Fisica, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina06', help_text='Físcia')
    disciplina_7 = models.OneToOneField(Quimica, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina07', help_text='Química')
    disciplina_8 = models.OneToOneField(Matematic, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='disciplina08', help_text='Filosofia')
    ## ////////////////////////////////////////////////////////
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.matricula

def aluno_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.matricula)

signals.pre_save.connect(aluno_pre_save, sender=AlunoCadastro)