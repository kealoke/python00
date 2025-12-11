import datetime
import time

time_now = time.time()

format_sec = "{:,.4f}".format(time_now)
exponential_sec = "{:.2e}".format(time_now)

dtime_now = datetime.datetime.now()
format_date = dtime_now.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {format_sec} or {exponential_sec}")
print(format_date)
