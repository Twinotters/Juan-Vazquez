# Generated by Django 2.1.5 on 2021-08-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=38)),
                ('user_name', models.CharField(max_length=35)),
            ],
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
    ]
