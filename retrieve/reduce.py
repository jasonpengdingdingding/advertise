# -*- coding: utf-8 -*-

from operator import itemgetter
from position import Position
import sys
 
word2count = {}
word2positions = {}
 
for line in sys.stdin:
    line = line.strip()
    word, position_index = line.split()
    try:
        document_id,frequency,positions = position_index.split(',')  
        word2count[word] = word2count.get(word, 0) + long(frequency)
        old_pos_list = word2positions.get(word, [])
        is_new_pos = True
        for old_pos in old_pos_list:
            if old_pos.document_id == document_id:
                old_pos.add_frequency(long(frequency))
                old_pos.add_positions(long(positions))
                is_new_pos = False
                break
        if is_new_pos:
            positions_list = []
            positions_list.append(long(positions))
            old_pos_list.append(Position(document_id, long(frequency), positions_list))
        
        word2positions[word] = old_pos_list
    except ValueError:
        pass
 
sorted_word2count = sorted(word2positions.items(), key=itemgetter(0))
 
for word, count in sorted_word2count:
    str = ''
    str += '%u;' % (len(count))
    positions_list_len = 0
    for pos in count:
        positions_list_len += pos.get_positions_len()
    str += '%u;' % (positions_list_len)
    for pos in count:
        str += pos.to_string()
    print '%s\t%s'% (word, str)
