# 날짜 시간 구하는 법
import datetime
import pytz

seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

print("{}{}{}{}{}{}".format(
now.year,
now.month,
now.day,
now.hour,
now.minute,
now.second))
