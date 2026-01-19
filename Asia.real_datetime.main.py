from datetime import datetime, timezone, timedelta
import sys
import time

HSR_CN = timezone(timedelta(hours=8)) # Asia Region (UTC+8)
print('HSR Time')
while True:
    hsr_utc8_time = datetime.now(HSR_CN).strftime('%Y/%m/%d %H:%M:%S') # year/month/day hour:minute:second
    sys.stdout.write('\r[ASIA] (UTC+8):' + 'ㅤ' + hsr_utc8_time)
    sys.stdout.flush()
    time.sleep(0.001) # Every 1 milisecond [Real Time]
