# -*- coding: utf-8 -*-
# opensslコマンドで対象ドメインの証明書情報を取得するプログラム
# python getCertinfo.py <FQDN> 
# 
# <FQDN> : target fqdn

import re
import subprocess
fqdn = sys.argv[1]
cmd  = ''

i = 0
def main():
    cmd = 'openssl s_client -connect ' + fqdn
    print(cmd)


if __name__ == '__main__':
    main()

