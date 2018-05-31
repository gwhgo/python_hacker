import zipfile
import optparse
from threading import Thread


flag = 0

def extractFile(zFile,passwd):
    try:
        zFile.extractall(pwd=passwd)
        print('[+] Password = ' + passwd + '\n')
        flag = 1
    except Exception as e:
        print(e)

def main():
    parser = optparse.OptionParser("usage%prg -f <zipfile> -d <dictionary>")
    parser.add_option("-f",dest="zname",type="string",help="specify zip file")
    parser.add_option("-d",dest="dname",type="string",help="specify dictionary file")
    (options,args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        if not flag:
            t = Thread(target=extractFile,args=(zFile,password))
            t.start()

if __name__ == '__main__':
    main()