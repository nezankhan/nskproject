# Generated by Django 4.1.2 on 2022-10-16 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseinvoices',
            old_name='po_id',
            new_name='po',
        ),
    ]
