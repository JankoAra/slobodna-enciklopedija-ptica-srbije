# Generated by Django 5.0.6 on 2024-05-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slobodna_enciklopedija_ptica_srbije', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='tip',
            field=models.CharField(choices=[('R', 'Registrovani Korisnik'), ('U', 'Urednik')], db_column='Tip', default='R', max_length=1),
        ),
    ]
