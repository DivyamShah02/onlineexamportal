# Generated by Django 3.0.5 on 2023-01-21 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='e_id',
            field=models.CharField(default='0', max_length=10),
            preserve_default=False,
        ),
    ]
