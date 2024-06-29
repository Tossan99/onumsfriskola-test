# Generated by Django 4.2.13 on 2024-06-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_staff_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='fname',
            field=models.CharField(help_text='Skriv förnamn för personen.', max_length=200, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='lname',
            field=models.CharField(help_text='Skriv efternamn för personen.', max_length=200, verbose_name='Last Name'),
        ),
    ]