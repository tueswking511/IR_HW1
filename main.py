import warc
import html2text

f = warc.open("C:/Users/123/Desktop/02.warc")
count = 0
for record in f:
    if record['Warc-type'] == 'warcinfo':
        pass
    else:
        print record
        temp = '\n'
        str = record.__str__()
        for i in range(24):
            if str != "":
                npos = str.index(temp)
                str = str[npos + 1:]
        h = html2text.HTML2Text()
        count = count + 1
        try:
            output = h.handle(str.decode("utf-8"))
            # print count.__str__() + " Web finish"
            # print type(output.__str__())
            # print output
            # print output.__str__().split()
            outputlist = output.__str__().split()
            # print outputlist
            # outputlist = filter(outputlist)
            for i in outputlist:
                # print 'Old:' + i.__str__()
                j = i.__str__()
                j = j.lower()
                j = filter(lambda ch: ch in 'abcdefghijklmnopqrstuvwxyz', j)
                if j != "":
                    print j.__str__()
        except UnicodeDecodeError:
            output = h.handle(str.decode("latin-1"))
            print count.__str__() + " Web finish"
            # print output
        break
