# Generated by Django 2.2.1 on 2019-05-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20190517_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacoes',
            name='image',
            field=models.ImageField(null=True, upload_to='media/publicacoes', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='image',
            field=models.ImageField(null=True, upload_to='media/servicos', verbose_name='Imagem'),
        ),
    ]
