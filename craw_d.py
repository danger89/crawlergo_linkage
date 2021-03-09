#!/usr/bin/python3
# coding: utf-8
import simplejson
import threading
import subprocess
import requests
import warnings
import json
from fake_useragent import UserAgent
import argparse

parser = argparse.ArgumentParser() # defines the parser
parser.add_argument('-p', help='The proxy port', dest='proxy',default='127.0.0.1:7777')
parser.add_argument('-p2', help='The proxy port', dest='proxy2',default='')
parser.add_argument('-u', help='targets url', dest='target_url')
args = parser.parse_args()
proxy = args.proxy
proxy2 = args.proxy2
target_url = args.target_url
ua = UserAgent(use_cache_server=False)

warnings.filterwarnings(action='ignore')

def get_random_headers():
    headers = {'User-Agent': ua.random}

    return headers


def main(url,pro):
	target = url
	cmd = ["./crawlergo", "-c", "chrome-linux/chrome","-t", "20","-f","smart","--fuzz-path","--custom-headers",json.dumps(get_random_headers()), "--push-to-proxy", "http://"+pro+"/", "--push-pool-max", "10","--output-mode", "json" , target]
	rsp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = rsp.communicate()
	try:
		result = simplejson.loads(output.decode().split("--[Mission Complete]--")[1])
	except:
		return
	print(result)



if __name__ == '__main__':
	if proxy2.strip()=='':
		main(target_url,proxy)
	else:
		main(target_url,proxy)
		main(target_url,proxy2)
	
