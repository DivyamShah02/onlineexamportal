# Generated by Django 4.1.7 on 2023-02-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0002_batch_b_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]