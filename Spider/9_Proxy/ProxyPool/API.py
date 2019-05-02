# -*- coding: utf-8 -*-

from flask import Flask, g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System!</h2>'


@app.route('/random')
def get_proxy():
    """
    获取随机可用代理
    :return: 一个可用代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_count():
    """
    获取代理总数
    :return: 代理总数
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()