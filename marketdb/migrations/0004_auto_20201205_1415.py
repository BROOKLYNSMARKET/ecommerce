# Generated by Django 3.1.4 on 2020-12-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdb', '0003_auto_20201204_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='SEM IMAGEM', upload_to=None),
        ),
    ]
