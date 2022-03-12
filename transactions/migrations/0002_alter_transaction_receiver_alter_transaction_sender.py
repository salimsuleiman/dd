# Generated by Django 4.0 on 2022-03-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.CharField(help_text='The wallet receive address who receive the funds', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.CharField(help_text='The user hash:id who sends the coins', max_length=200),
        ),
    ]
