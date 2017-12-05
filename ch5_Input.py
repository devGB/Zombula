import urllib.request

file = urllib.request.Request('http://helloworldbook.com/data/message.txt')
#file = urllib.request.Request('http://google.com')
message = urllib.request.urlopen(file)
print(message.read())
