# Generated by Django 4.2.16 on 2025-02-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jennifer', '0003_alter_models_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='image',
            field=models.ImageField(blank=True, upload_to='jennifer/files/covers'),
        ),
    ]
