# Generated by Django 3.2.16 on 2022-12-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_carro_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotoscarro',
            name='is_principal',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]