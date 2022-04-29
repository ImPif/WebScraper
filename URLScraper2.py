import urllib.request

url = urllib.request.urlopen("http://python.org")

url = url.read()

htmltext = url.decode('utf8)')
print(htmltext)