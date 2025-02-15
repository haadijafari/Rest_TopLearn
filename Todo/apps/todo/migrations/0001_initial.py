# Generated by Django 4.2.14 on 2024-07-15 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('priority', models.IntegerField(default=1, verbose_name='Priority')),
                ('is_done', models.BooleanField(default=False, verbose_name='is Done?')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'db_table': 'todos',
                'ordering': ['priority', 'title'],
            },
        ),
    ]
