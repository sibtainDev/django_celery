# Generated by Django 4.0 on 2023-02-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation', models.CharField(choices=[('FIB', 'Fibonacci')], max_length=3)),
                ('input', models.IntegerField()),
                ('output', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ERROR', 'Error'), ('SUCCESS', 'Success')], max_length=8)),
                ('message', models.CharField(blank=True, max_length=110)),
            ],
        ),
    ]
