f = open("new.txt", "w+")
for i in range(100):
    f.write("This is a very interesting line: %d\r\n" % (i+1))


f.close()