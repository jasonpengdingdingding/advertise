# -*- coding: utf-8 -*-
"""
position index for term in document
"""

class Position:
    '''Position index '''

    def __init__(self, document_id = '', frequency = 0, positions = []):
        self.document_id = document_id
        self.frequency = frequency
        self.positions = positions

    def add_frequency(self, freq):
        '''update frequency'''
        self.frequency += freq

    def add_positions(self, pos):
        '''add new positions list'''
        self.positions.append(pos)
        self.positions.sort()

    def get_positions_len(self):
        ''''''
        return len(self.positions)

    def to_string(self):
        return '(%s,%s,%s)' % (self.document_id, self.frequency, self.positions)
