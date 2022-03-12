# Generated by Django 4.0 on 2022-03-06 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('token_hash', models.CharField(help_text='The hash key of the refresh token, to help stop premaid refresh token', max_length=500)),
                ('token_salt', models.CharField(help_text='The token hash salt to secure cracking', max_length=500)),
                ('refresh_token', models.CharField(help_text='Refresh Token for authorization', max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='users.user', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
    ]