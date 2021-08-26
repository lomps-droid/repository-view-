# Generated by Django 3.2.6 on 2021-08-20 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210818_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porturgue',
            name='media',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Média'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota01',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 01'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota02',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 02'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota03',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 03'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota04',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 04'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota05',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 05'),
        ),
        migrations.AlterField(
            model_name='porturgue',
            name='nota06',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=5, verbose_name='Nota 06'),
        ),
    ]