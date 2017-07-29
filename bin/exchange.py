#!/usr/bin/env python3

import urllib.request
import json
import os

with urllib.request.urlopen("https://www.gaitameonline.com/rateaj/getrate") as response:
	data = response.read().decode("utf-8")

	exchange = json.loads(data)

	for currency in exchange["quotes"]:
		if currency["currencyPairCode"] == "USDJPY":
			command = "echo \"usdjpy\t1ドル " + currency["ask"] + "円\" | nc localhost 39114"
			os.system(command)
