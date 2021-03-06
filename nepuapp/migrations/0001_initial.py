# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-14 13:31
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '内容管理',
                'verbose_name_plural': '内容管理',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='新闻分类')),
            ],
            options={
                'verbose_name': '新闻分类',
                'verbose_name_plural': '新闻分类',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
            ],
            options={
                'verbose_name': '栏目导航',
                'verbose_name_plural': '栏目导航',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_reason', models.CharField(choices=[('校园新闻', '校园新闻'), ('通知公告', '通知公告')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('modified_time', models.DateTimeField(verbose_name='发布时间')),
                ('source_link', models.CharField(max_length=200)),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='文章摘要')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cate', to='nepuapp.Category', verbose_name='新闻分类')),
            ],
            options={
                'verbose_name': '新闻发布',
                'verbose_name_plural': '新闻发布',
            },
        ),
        migrations.AddField(
            model_name='paper',
            name='select_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_post', to='nepuapp.Post'),
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nepuapp.Column', verbose_name='归属栏目'),
        ),
    ]
