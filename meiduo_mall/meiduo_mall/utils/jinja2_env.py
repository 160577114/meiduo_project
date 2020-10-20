from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def jinja2_environment(**optins):
    # jinja2环境

    # 创建环境对象
    env = Environment(**optins)
    # 自定义语法
    env.globals.update({
        'static': staticfiles_storage.url,  # 获取静态文件的前缀
        'url': reverse,  # 反向解析
    })

    # 返回环境对象
    return env
