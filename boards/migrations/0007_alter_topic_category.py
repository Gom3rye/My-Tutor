# Generated by Django 3.2.9 on 2021-12-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_auto_20211218_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(blank=True, help_text='글의 분류를 설정하세요.', to='boards.Category'),
        ),
    ]
