# Generated by Django 4.2.7 on 2023-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, to='library_app.author'),
        ),
    ]