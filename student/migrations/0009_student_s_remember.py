# Generated by Django 3.0.5 on 2023-02-15 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20230130_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_remember',
            field=models.CharField(default='0', max_length=255),
            preserve_default=False,
        ),
    ]
