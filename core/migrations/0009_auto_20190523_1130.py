# Generated by Django 2.2.1 on 2019-05-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190519_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='image',
            field=models.ImageField(null=True, upload_to='servicos/', verbose_name='Imagem'),
        ),
    ]
