# Generated by Django 2.2.5 on 2019-09-29 18:05

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arraymodel',
            name='sample_array',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None),
        ),
    ]