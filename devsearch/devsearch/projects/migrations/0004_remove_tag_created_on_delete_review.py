# Generated by Django 4.1.4 on 2023-01-02 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag_project_vote_ratio_project_vote_total_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created_on',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
