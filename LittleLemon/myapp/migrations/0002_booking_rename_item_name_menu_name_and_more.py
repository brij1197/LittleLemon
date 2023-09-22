# Generated by Django 4.2.3 on 2023-08-05 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.SmallIntegerField(default=10)),
            ],
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
