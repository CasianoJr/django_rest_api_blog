# Generated by Django 3.1.4 on 2020-12-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201206_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(blank=True, default='default.png', upload_to='author/'),
        ),
    ]