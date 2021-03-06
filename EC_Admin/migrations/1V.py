# Generated by Django 2.2.3 on 2020-02-01 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('voterid_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(max_length=1024)),
                ('mobile_no', models.BigIntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('parliamentary', models.CharField(max_length=50)),
                ('assembly', models.CharField(max_length=50)),
                ('voter_image', models.ImageField(upload_to='VoterImage/')),
            ],
        ),
    ]
