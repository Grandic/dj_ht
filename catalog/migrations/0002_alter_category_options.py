# Generated by Django 4.2.4 on 2023-09-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
    ]
