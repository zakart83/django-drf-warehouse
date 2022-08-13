# Generated by Django 4.1 on 2022-08-13 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Status')),
            ],
            options={
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='Order number')),
                ('warehouse', models.IntegerField()),
                ('store', models.CharField(max_length=255, verbose_name='Store')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='warehouse.status', verbose_name='Status')),
            ],
        ),
         migrations.RunSQL(
            "INSERT INTO warehouse_status ('title') VALUES ('In progress');",
        ),
        migrations.RunSQL(
            "INSERT INTO warehouse_status ('title') VALUES ('Stored');",
        ),
        migrations.RunSQL(
            "INSERT INTO warehouse_status ('title') VALUES ('Sent');",
        ),
    ]