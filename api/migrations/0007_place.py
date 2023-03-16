# Generated by Django 4.1.7 on 2023-03-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_poiopeninghour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('json', models.CharField(max_length=8192)),
                ('last_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'place',
                'managed': False,
            },
        ),
    ]