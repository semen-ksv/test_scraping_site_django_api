# Generated by Django 3.0.8 on 2020-07-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citrys_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='specifications',
            field=models.TextField(blank=True, null=True),
        ),
    ]
