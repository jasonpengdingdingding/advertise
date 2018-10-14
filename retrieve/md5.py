# -*- coding: utf-8 -*-

import hashlib

def gen_md5(str):
	'''generate md5 for a string'''
	hl=hashlib.md5()
	hl.update(str.encode(encoding='utf-8'))
	return hl.hexdigest()
