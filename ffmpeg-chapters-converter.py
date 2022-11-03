import re

chapters = list()

with open('chapters.txt', 'r') as f:
   for line in f:
      x = re.match(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3}) (.*)", line)
      hrs = int(x.group(1))
      mins = int(x.group(2))
      secs = int(x.group(3))
      milisecs = int(x.group(4))
      title = x.group(5)

      minutes = (hrs * 60) + mins
      seconds = secs + (minutes * 60)
      timestamp = (seconds * 1000 + milisecs)
      chap = {
         "title": title,
         "startTime": timestamp
      }
      chapters.append(chap)

text = ""

for i in range(len(chapters)-1):
   chap = chapters[i]
   title = chap['title']
   start = chap['startTime']
   end = chapters[i+1]['startTime']-1
   text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""


with open("chapters.ffmpeg.txt", "a") as myfile:
    myfile.write(text)