import time
# time='2020-07-16 16:17:46,'
timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(timestamp)