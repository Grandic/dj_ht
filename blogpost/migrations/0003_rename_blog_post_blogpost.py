# Generated by Django 4.2.4 on 2023-09-13 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_rename_blogpost_blog_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog_post',
            new_name='Blogpost',
        ),
    ]
