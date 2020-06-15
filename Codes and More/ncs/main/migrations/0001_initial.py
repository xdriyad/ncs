# Generated by Django 2.2.1 on 2019-12-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('rfid', models.CharField(max_length=15)),
                ('nurse', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('node', models.OneToOneField(on_delete=None, to='main.Node')),
                ('ward', models.ManyToManyField(to='main.Ward')),
            ],
        ),
        migrations.CreateModel(
            name='IpTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='', max_length=25)),
                ('node', models.OneToOneField(on_delete=None, to='main.Node')),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('call_time', models.DateTimeField(blank=True, null=True)),
                ('rec_time', models.DateTimeField(blank=True, null=True)),
                ('serv_time', models.DateTimeField(blank=True, null=True)),
                ('bed', models.ForeignKey(blank=True, null=True, on_delete=None, to='main.Bed')),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=None, to='main.Nurse')),
            ],
        ),
        migrations.AddField(
            model_name='bed',
            name='node',
            field=models.OneToOneField(on_delete=None, to='main.Node'),
        ),
        migrations.AddField(
            model_name='bed',
            name='ward',
            field=models.ManyToManyField(to='main.Ward'),
        ),
    ]