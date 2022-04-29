from lib2to3.pgen2.token import DOT
import urllib.request

text_file = open("D:/Programming/FuckAroundShit/URL Scraper/test.txt", 'wb')

x = urllib.request.urlopen("https://www.sousetsuka.com/2018/05/okami-wa-nemuranai-12.html")

#mybytes = x.read()

#mystring = mybytes.decode("utf8")

#x.close()

#lines2 = ''

DoTheThing = False

for lines in x.readlines():
#    line2 = lines.decode("utf8")
    if 'post-body entry-content' in lines.decode('utf8'):
        DoTheThing = True
    if DoTheThing == True:
        text_file.write(lines)
    if 'Next Chapter' in lines.decode('utf8'):
        break

text_file.close()