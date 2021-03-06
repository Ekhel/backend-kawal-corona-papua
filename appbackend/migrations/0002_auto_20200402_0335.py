# Generated by Django 2.2.8 on 2020-04-01 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appbackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kabupaten',
            options={'ordering': ('id_kabupaten',)},
        ),
        migrations.AlterModelOptions(
            name='penderita',
            options={'ordering': ('id_penderita',)},
        ),
        migrations.AlterField(
            model_name='penderita',
            name='status',
            field=models.CharField(choices=[('sembuh', 'SEMBUH'), ('meninggal', 'MENINGGAL'), ('perawatan', 'PERAWATAN')], default='sembuh', max_length=15),
        ),
        migrations.CreateModel(
            name='Rumah_sakit',
            fields=[
                ('id_rs', models.AutoField(primary_key=True, serialize=False)),
                ('rumah_sakit', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=128)),
                ('lon', models.CharField(max_length=120)),
                ('lokasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appbackend.Kabupaten')),
            ],
            options={
                'ordering': ('id_rs',),
            },
        ),
    ]
