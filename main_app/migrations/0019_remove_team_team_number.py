# Generated by Django 3.0.2 on 2020-01-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_delete_matchandwinner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='team_number',
        ),
    ]