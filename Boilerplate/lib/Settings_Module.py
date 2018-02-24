import os
import codecs
import json

class MySettings(object):
	def __init__(self, settingsfile=None):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
				self.__dict__ = json.load(f, encoding="utf-8")
		except:
			self.Command = "!ping"
			self.Response = "pong! ^_^"
			self.Cooldown = 10
			self.Permission = "everyone"
			self.Info = ""

	def Reload(self, jsondata):
		self.__dict__ = json.loads(jsondata, encoding="utf-8")
		return

	def Save(self, settingsfile):
		try:
			with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
				json.dump(self.__dict__, f, encoding="utf-8")
			with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
				f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
		except:
			Parent.Log(ScriptName, "Failed to save settings to file.")
		return