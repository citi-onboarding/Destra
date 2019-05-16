# Generated by Django 2.2.1 on 2019-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190516_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Site Name', max_length=255)),
                ('maintenance_mode', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Quem somos',
            },
        ),
        migrations.DeleteModel(
            name='QuemSomos',
        ),
    ]
