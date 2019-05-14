#!/usr/bin/python3

from collections import deque
from argparse import ArgumentParser
from package.scan import dirLook
from package.additional import *

banner()

argument = ArgumentParser( description = "Finding out interesting directory and file in a website." )
argument.add_argument("-u", "--url", help = "url target")
argument.add_argument("-w", "--wordlist", help = "list wordlist")
argument.add_argument("-r", "--ragent", help = "random user-agent", action = "store_true")
argobjek = argument.parse_args()

if not argobjek.url or not argobjek.wordlist:
	usage()
	exit()

threads = deque([]) # it's not a stack, its queue
target  = argobjek.url + "/" if not argobjek.url.endswith("/") else argobjek.url + ""
wordlist = list(map(remove_newline,open(argobjek.wordlist).readlines()))

try:
	for dir_and_file in wordlist:
		scan = dirLook(target, dir_and_file.strip(), argobjek.ragent)
		threads.append(scan)

	for thread in range(0, len(threads)):
		queue = threads.popleft()
		queue.start()
except(KeyboardInterrupt, SystemExit):
	if queue.is_alive() == False:
		exit_loading()
	else:
		pass
