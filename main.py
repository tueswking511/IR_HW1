import warc
import html2text

f = warc.open("C:/Users/123/Desktop/02.warc")
count = 0
for record in f:
    if record['Warc-type'] == 'warcinfo':
        pass
    else:
        temp = '\n'
        str = record.__str__()
        for i in range(24):
            if str != "":
                npos = str.index(temp)
                str = str[npos+1:]
        h = html2text.HTML2Text()
        count = count + 1
        try:
            output = h.handle(str.decode("utf-8"))
            print count.__str__() + " Web finish"
            # print output
        except UnicodeDecodeError:
            output = h.handle(str.decode("latin-1"))
            print count.__str__() + " Web finish"
            # print output
print count
