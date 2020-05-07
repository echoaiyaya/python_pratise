import re

f1 = open('大王饶命.txt', 'r+', encoding="utf-8")
infos = f1.readlines()
f1.seek(0,0)
i = 1
for line in infos:
	title = re.match(r'章节名:(.*?)、', line, re.S)
	if title:
		line = line.replace(r'章节名', '第' + str(title.group(1)) + '章节 ')
		
		print(line)
		i += 1
	f1.write(line)
f1.close()