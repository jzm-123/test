import random
import time

second = random.randint(0,60)
print('before:',time.time())
time.sleep(second)
print('after:',time.time())
