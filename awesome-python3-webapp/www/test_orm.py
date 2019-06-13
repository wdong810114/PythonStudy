#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Dongdong Wang'

import orm
import asyncio
import random
from models import User, Blog, Comment

async def test(loop):
    pool = await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')
    u = User(name='test', email='test%s@example.com' % random.randint(0,10000000), passwd='abc123456', image='about:blank')
    await u.save()

# 要运行协程，需要使用事件循环 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished.')
    loop.close()