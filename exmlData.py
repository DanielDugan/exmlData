import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_205716.xml '

while True:
    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    print "counts[0] = ", counts[0]
    print "counts[0].text = ", counts[0].text
    print "type(int(counts[0].text)) = ", type(int(counts[0].text))
    total = 0
    for index in range(0, len(counts)):
      total += int(counts[index].text)
    print total
    break
