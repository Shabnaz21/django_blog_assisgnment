# Generated by Django 4.2.1 on 2023-05-09 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_post_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['published'], 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'catogries'},
        ),
    ]
