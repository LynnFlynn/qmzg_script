#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import configparser

CONFIG_FILE = "config.ini"
class cfgConst:
	testModel = False

	@classmethod
	def getConfig(cls):
		if os.path.exists(os.path.join(os.getcwd(), CONFIG_FILE)):
			config = configparser.ConfigParser()
			config.read(CONFIG_FILE)
			cls.testModel = cls.cfg_str2bool(config.get("Common", "testModel"))

	@staticmethod
	def cfg_str2bool(str):
		if str.lower() == "true":
			return True
		elif str.lower() == "false":
			return False
		else:
			return False

if __name__ == '__main__':
	cfgConst.getConfig()

cfgConst.getConfig()