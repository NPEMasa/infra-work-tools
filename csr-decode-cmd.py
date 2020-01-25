# -*- coding: utf-8 -*-
import sys
import re
fname = sys.argv[1]
outfile = 'csrdec.txt'
i = 0
def main():
    with open(fname) as f:
        l = f.readlines()
        row = ''
        cnt = 0
        for row in l:
            row = row.rstrip('\r\n')
            
            print(str(cnt) + '\t: ' + row)
            f_arr = 'openssl req -in {0} -noout -text'
            res1 = f_arr.format(row)
            res1 = res1+'\n'
            with open(outfile, mode='a') as f:
                f.write(res1)

if __name__ == '__main__':
    main()

