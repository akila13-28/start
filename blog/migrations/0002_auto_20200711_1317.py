# Generated by Django 3.0.8 on 2020-07-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='heading',
            new_name='catagory',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='desc',
            new_name='catalog',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='ques',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='question',
        ),
    ]
