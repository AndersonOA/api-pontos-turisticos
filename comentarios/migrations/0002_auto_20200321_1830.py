# Generated by Django 3.0.4 on 2020-03-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='aprovado',
            field=models.BooleanField(default=True),
        ),
    ]
