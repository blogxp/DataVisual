# Generated by Django 2.2.4 on 2019-08-17 08:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('infos', '0002_auto_20190817_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infosconfig',
            old_name='pki_id',
            new_name='pk_id',
        ),
    ]
