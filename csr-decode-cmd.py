# -*- coding: utf-8 -*-
########## opensslコマンドを2つ出力するプログラム  ##########
## python csr-decode-cmd.py <filename> 
## 
## <filename> : FQDN list text file
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
	    ### ファイル読み込み時の改行コードを削除する ###
            row = row.rstrip('\r\n')
            
            print(str(cnt) + '\t: ' + row)
            f_arr = 'openssl req -in {0} -noout -text'
            res1 = f_arr.format(row)
            res1 = res1+'\n'
            with open(outfile, mode='a') as f:
                f.write(res1)

if __name__ == '__main__':
    main()

