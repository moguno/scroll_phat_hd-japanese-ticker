#!/usr/bin/env python3

import urllib.request
import json
import os

with urllib.request.urlopen("http://weather.livedoor.com/forecast/webservice/json/v1?city=280010") as response:
	data = response.read().decode("utf-8")

	weather = json.loads(data)

	max_tmp = weather["forecasts"][1]["temperature"]["max"]["celsius"]
	min_tmp = weather["forecasts"][1]["temperature"]["min"]["celsius"]

	forecast = weather["forecasts"][0]["telop"]

	command = "echo \"forecast\t今日の天気 " + forecast + "\" | nc localhost 39114"
	os.system(command)

	command = "echo \"temperature\t今日の気温 最高" + max_tmp + "℃ 最低" + min_tmp + "℃\" | nc localhost 39114"
	os.system(command)
