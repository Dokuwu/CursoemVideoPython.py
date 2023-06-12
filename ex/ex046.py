from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize('\033[1;33m:collision:\033[m\033[1;31;40mFELIZ ANO NOVO!!!\033[m\033[1;33m:collision:\033[m', language='en'))
