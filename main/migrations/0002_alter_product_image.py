# Generated by Django 4.2.7 on 2023-12-04 09:15

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=main.utils.generate_filename),
        ),
    ]