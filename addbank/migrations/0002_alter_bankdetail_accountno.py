# Generated by Django 4.0.6 on 2022-11-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addbank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='accountno',
            field=models.IntegerField(max_length=100),
        ),
    ]