#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   BTC Wallet Sample
   Decrypt wallet class
   Created by chi on 2/16/2017
"""

import json

class Json:
	def __init__(self, data):
		self.data = data

	def dump(self):
		print(json.dumps(self.data))


	# if __name__ == '__main__':

# test = Json("['foo', {'bar': ('baz', None, 1.0, 2)}]")
# test.dump()