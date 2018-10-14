# -*- coding: utf-8 -*- 

import sys
from md5 import gen_md5

for line in sys.stdin:
    document_id = gen_md5(line)
    line = line.strip()
    words = line.split()
    for idx in range(len(words)):
        if len(words[idx])==0:
            continue
        #word (documnet_id,count,position in document)
        print '%s\t%s,%d,%d' % (words[idx], document_id, 1, idx)
