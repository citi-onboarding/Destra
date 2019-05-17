# Generated by Django 2.2.1 on 2019-05-16 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190516_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('missao', models.TextField()),
                ('visao', models.TextField()),
                ('valores', models.TextField()),
                ('maintenance_mode', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Quem somos',
            },
        ),
        migrations.DeleteModel(
            name='SiteConfiguration',
        ),
    ]