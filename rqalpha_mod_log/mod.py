# !/usr/bin/env python
# -*- coding: utf-8 -*-

from rqalpha.interface import AbstractMod
from rqalpha.utils.logger import user_system_log, user_log

from logbook.handlers import Handler, StringFormatterHandlerMixin
from logbook.base import NOTSET

from rqalpha.environment import Environment


# FIXME:原 user_std_handler_log_formatter 已无效，git 可追溯到 2020-02-27 的 refactor

class LogHandler(Handler, StringFormatterHandlerMixin):
    def __init__(self, send_log_handler, mod_config, level=NOTSET, format_string=None, filter=None, bubble=False):
        Handler.__init__(self, level, filter, bubble)
        StringFormatterHandlerMixin.__init__(self, format_string)
        self.send_log_handler = send_log_handler
        self.mod_config = mod_config
        # self.formatter = user_std_handler_log_formatter

    def _write(self, level_name, item):
        dt = Environment.get_instance().calendar_dt
        self.send_log_handler(dt, item, level_name, mod_config=self.mod_config)

    def emit(self, record):
        # FIXME:原锁也已失效，所以并不是线程安全的，但本来rqalpha乃至plus都不是线程安全的，见 https://www.ricequant.com/doc/rqalpha-plus/tutorial.html#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98
        msg = self.format(record)
        # self.lock.acquire()
        # try:
        self._write(record.level_name, msg)
        # finally:
        #     self.lock.release()


class CustomLogHandlerMod(AbstractMod):
    def _send_log(self, dt, text, log_tag, mod_config):
        with open(f'{mod_config.log_file}', mode=mod_config.log_mode) as f:
            f.write(f'[{dt}] {log_tag}: {text}\n')

    def start_up(self, env, mod_config):
        user_log.handlers.append(LogHandler(self._send_log, mod_config, bubble=True))
        user_system_log.handlers.append(LogHandler(self._send_log, mod_config, bubble=True))

    def tear_down(self, code, exception=None):
        pass


def load_mod():
    return CustomLogHandlerMod()
