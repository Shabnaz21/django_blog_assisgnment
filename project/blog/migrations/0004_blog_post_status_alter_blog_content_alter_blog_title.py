# Generated by Django 4.2.1 on 2023-05-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_slug_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(help_text='Enter Your Content Here'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, help_text='Enter Your Post Title Here', max_length=200, null=True),
        ),
    ]
