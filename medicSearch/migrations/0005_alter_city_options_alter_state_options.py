# Generated by Django 4.1.7 on 2023-03-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0004_alter_state_name_alter_state_uf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('state', 'name')},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ('name',)},
        ),
    ]
