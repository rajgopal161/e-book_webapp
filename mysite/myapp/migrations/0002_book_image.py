# Generated by Django 3.0 on 2021-12-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='book_images/'),
        ),
    ]

