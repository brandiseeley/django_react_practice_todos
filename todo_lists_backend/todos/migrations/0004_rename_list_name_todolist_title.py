# Generated by Django 5.0.6 on 2024-07-08 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_rename_title_todolist_list_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='list_name',
            new_name='title',
        ),
    ]