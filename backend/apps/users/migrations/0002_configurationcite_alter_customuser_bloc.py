# Generated by Django 5.0 on 2024-12-28 20:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurationCite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_blocs', models.IntegerField(help_text='Nombre total de blocs dans la cité', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Configuration de la cité',
                'verbose_name_plural': 'Configuration de la cité',
            },
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bloc',
            field=models.CharField(blank=True, help_text='Numéro du bloc', max_length=10),
        ),
    ]
