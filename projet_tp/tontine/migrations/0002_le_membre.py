# Generated by Django 4.1.4 on 2023-01-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Le_membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('Prénom', models.CharField(max_length=170)),
                ('Email', models.CharField(max_length=70)),
                ('tontine', models.CharField(max_length=70)),
                ('Nombre_parts', models.CharField(max_length=70)),
                ('statut', models.CharField(max_length=70)),
            ],
        ),
    ]
