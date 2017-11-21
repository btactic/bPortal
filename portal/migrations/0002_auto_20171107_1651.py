# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=50)),
                ('action', models.CharField(choices=[('read', 'Read'), ('create', 'Create'), ('edit', 'Edit'), ('delete', 'Delete')], max_length=30)),
                ('grant', models.BooleanField()),
                ('order', models.IntegerField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Role')),
            ],
        ),
        migrations.CreateModel(
            name='RoleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rolepermission',
            unique_together=set([('role', 'module', 'action')]),
        ),
    ]