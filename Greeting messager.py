import time
tim=time.strftime('%H:%M:%S')
print(tim)
greeting=""
timh=int(time.strftime('%H'))
if 5<= timh < 12:
# if (timh>0 and timh>12):
    greeting="Good morning"
elif 12 <= timh <16:
# elif (timh<12 and timh>16):
    greeting="Good afteernoon"
elif 16 <= timh <18:
# elif (timh<16 and timh>18):
    greeting="Good evening" 
else:
    greeting="Good Night"
print(greeting)        