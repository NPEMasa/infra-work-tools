# -*- coding: utf-8 -*-

import re
import sys
import subprocess

class certinfo():

    param = sys.argv[1]

    def getCert(self):

        cmd = 'echo "Q" | openssl s_client -connect ' + self.param + ':443 > certinfo.txt'
        cp = subprocess.call(cmd, encoding='UTF-8', shell=True)
        print(cp)
            
def main():

    m = certinfo()
    m.getCert()

if __name__ == '__main__':
    main()