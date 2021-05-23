# Generated by Django 3.2.3 on 2021-05-23 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_lang_store_lat'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='shop_status',
            field=models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=10),
        ),
    ]
