from urllib import urlopen
import re
p=re.compile('<a.*?href="(.*?)">(.*?)</a>')
text=urlopen('http://zsp.iteye.com/blog/309997').read()
for url,name in p.findall(text):
    print '%s (%s)' % (name,url)
