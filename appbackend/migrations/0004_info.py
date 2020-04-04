# Generated by Django 2.2.8 on 2020-04-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbackend', '0003_auto_20200403_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('odp', models.CharField(max_length=20)),
                ('pdp', models.CharField(max_length=20)),
                ('positif', models.CharField(max_length=20)),
                ('sembuh', models.CharField(max_length=20)),
                ('meninggal', models.CharField(max_length=20)),
                ('keteranga', models.TextField()),
            ],
            options={
                'ordering': ('id_item',),
            },
        ),
    ]
