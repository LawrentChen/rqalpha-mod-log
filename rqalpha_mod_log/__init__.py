# !/usr/bin/env python
# -*- coding: utf-8 -*-

# FIXME:应该使用这里的__config__，原文档https://rqalpha.readthedocs.io/zh_CN/latest/development/collecting_logs.html已过时
# FIXME:参考mod拓展命令行参数 https://rqalpha.readthedocs.io/zh_CN/latest/intro/run_algorithm.html?highlight=click#id6

import click
from rqalpha import cli

__config__ = {
    # 如果指定路径，则输出 log 日志文件
    "log_file": None,
    # 指定文件写入模式，默认为追加写入
    "log_mode": 'a'
}

cli.commands['run'].params.append(
    click.Option(
        ('--log-file', 'mod__log__log_file'),
        default=None,
        help="[log] filepath to save log file"
    )
)

cli.commands['run'].params.append(
    click.Option(
        ('--log-mode', 'mod__log__log_mode'),
        default=None,
        help="[log] how to 'open' the log file"
    )
)


def load_mod():
    from .mod import CustomLogHandlerMod
    return CustomLogHandlerMod()
