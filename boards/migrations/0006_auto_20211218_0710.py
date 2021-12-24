# Generated by Django 3.2.9 on 2021-12-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_auto_20211218_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(help_text='글의 분류를 설정하세요.', to='boards.Category'),
        ),
    ]
