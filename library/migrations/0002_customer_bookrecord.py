# Generated by Django 5.0.3 on 2024-03-13 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('student', 's'), ('teacher', 't')], default='S', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BookRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True)),
                ('returned_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.customer')),
            ],
        ),
    ]
