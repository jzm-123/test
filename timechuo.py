
from datetime import datetime
import time
t=1299976544334
timeStamp = float(t / 1000)  # 毫秒时间戳转为秒级时间戳
timeArray = time.localtime(timeStamp)  # float变为时间戳
ntCtime_str = time.strftime("%Y-%m-%d", timeArray)  # 时间戳转成Y-M-D的str
ntCtime_dt = datetime.strptime(ntCtime_str, "%Y-%m-%d")  # str转datetime.datetime类型
print(ntCtime_str)
print(ntCtime_dt)