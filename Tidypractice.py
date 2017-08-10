from subprocess import Popen,PIPE
from urllib import urlopen

text=open("htmltable.htm").read()
tidy=Popen('tidy',stdin=PIPE,stdout=PIPE,stderr=PIPE)

tidy.stdin.write(text)
tidy.stdin.close()

print tidy.stdout.read()