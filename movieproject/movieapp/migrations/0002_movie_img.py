# Generated by Django 4.1.5 on 2023-01-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ss', upload_to='pics'),
            preserve_default=False,
        ),
    ]
