from datetime import datetime
now = datetime.now()
f = open("test.txt", "a")

current_time = now.strftime("%H:%M:%S")

f.write("Current Time ="+current_time)
f.close()

print('hi')