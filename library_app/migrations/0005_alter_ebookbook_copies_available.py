# Generated by Django 4.2.7 on 2023-11-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_alter_ebookbook_copies_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebookbook',
            name='copies_available',
            field=models.IntegerField(),
        ),
    ]
