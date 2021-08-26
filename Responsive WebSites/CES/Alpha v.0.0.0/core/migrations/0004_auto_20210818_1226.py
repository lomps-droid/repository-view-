# Generated by Django 3.2.6 on 2021-08-18 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210818_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_1',
            field=models.OneToOneField(blank=True, default=None, help_text='Português', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina01', to='core.porturgue'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_2',
            field=models.OneToOneField(blank=True, default=None, help_text='Matemática', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina02', to='core.matematic'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_3',
            field=models.OneToOneField(blank=True, default=None, help_text='Geografia', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina03', to='core.geografia'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_4',
            field=models.OneToOneField(blank=True, default=None, help_text='História', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina04', to='core.historia'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_5',
            field=models.OneToOneField(blank=True, default=None, help_text='Biologia', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina05', to='core.biologia'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_6',
            field=models.OneToOneField(blank=True, default=None, help_text='Físcia', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina06', to='core.fisica'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_7',
            field=models.OneToOneField(blank=True, default=None, help_text='Química', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina07', to='core.quimica'),
        ),
        migrations.AlterField(
            model_name='alunocadastro',
            name='disciplina_8',
            field=models.OneToOneField(blank=True, default=None, help_text='Filosofia', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disciplina08', to='core.matematic'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nome',
            field=models.CharField(blank=True, default='Ex: Português', max_length=100, verbose_name='Matéria'),
        ),
    ]
