# Generated by Django 2.2.10 on 2020-12-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201224_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='first_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='second_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='third_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='first_choice',
            field=models.TextField(blank=True, null=True),
        ),
    ]
