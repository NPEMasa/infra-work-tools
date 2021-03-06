# -*- coding: utf-8 -*-
########## コマンドを2つ出力するプログラム  ##########
## python csrcmdOut.py <filename> 
## 
## <filename> : FQDN list text file
import sys
import re
fname = sys.argv[1]
outfile = 'resultlst.txt'

i = 0
def main():
    with open(fname) as f:
        l = f.readlines()
        
    #print(l)  ## debug only
    long1 = len(l) - 1
    #print(long1) ## debug only
    row = ''
    for row in l:
        
        ## 配列内の改行コードを削除
        row = row.rstrip('\r\n')
	
	## ECDSAにてCSRを作成するコマンドを出力
        f_arr = 'openssl ecparam -name secp384r1 -genkey | openssl ec -out {0}.key -des3'
        s_arr = 'openssl req -new -key {0}.key -sha256 -out {1}.csr -subj "/C=JP/L=Tokyo/O=hogehoge co.ltd,/OU=develop div./CN={2}" -out {3}.csr'
        res1 = f_arr.format(row)
        res2 = s_arr.format(row,row,row,row)
        res1 = res1+'\n'
        print(res1)
        #print('\n') ## debug only
        res2 = res2+'\n\n'
        print(res2)
        #print('\n\n') ## debug only
        with open(outfile, mode='a') as f:
            f.write(res1)
            f.write(res2)

if __name__ == '__main__':
    main()

