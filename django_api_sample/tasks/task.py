# 呼び出し先(=Task)
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def hello(proj_id):
    time.sleep(10)  # 非同期に処理が終わることを確認するために10秒まつ
    message = "hello"
    print(message)  # 標準出力
    return message  # 結果を返す
