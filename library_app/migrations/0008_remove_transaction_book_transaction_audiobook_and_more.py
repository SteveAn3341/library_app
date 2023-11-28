# Generated by Django 4.2.7 on 2023-11-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_rename_return_date_transaction_returned_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='book',
        ),
        migrations.AddField(
            model_name='transaction',
            name='audioBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.audiobook'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ebook_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.ebookbook'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='hardcover_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.hardcoverbook'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='paperbackBook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.paperbackbook'),
        ),
    ]
