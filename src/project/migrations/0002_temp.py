# Generated by Django 5.0.6 on 2024-06-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('temp1', models.ManyToManyField(related_name='temp1', to='project.project')),
            ],
        ),
    ]
