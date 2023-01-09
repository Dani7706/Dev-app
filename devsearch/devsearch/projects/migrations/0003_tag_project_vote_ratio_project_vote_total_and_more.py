# Generated by Django 4.1.4 on 2023-01-02 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(to='projects.tag'),
        ),
    ]