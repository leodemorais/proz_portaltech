from datetime import datetime

import random
import time

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18,
        20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
          40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

for i in range(100):
    right_this_minute = datetime.today().minute
    if right_this_minute in evens:
        print("Estamos em um minuto par!")
    else:
        print("Estamos em um minuto impar!")
    wait_time = random.randint(1, 10)
    time.sleep(wait_time)



