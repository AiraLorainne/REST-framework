# Generated by Django 5.0.5 on 2024-05-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_name_item_phone_remove_item_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
