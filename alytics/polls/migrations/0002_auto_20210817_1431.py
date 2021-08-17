# Generated by Django 3.2.6 on 2021-08-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedfunction',
            name='dt',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='savedfunction',
            name='interval',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='savedfunction',
            name='exception',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='savedfunction',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='savedfunction',
            name='textual',
            field=models.CharField(max_length=100),
        ),
    ]