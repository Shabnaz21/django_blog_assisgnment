# Generated by Django 4.2.1 on 2023-05-09 06:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(help_text='Enter Your Content Here'),
        ),
    ]
