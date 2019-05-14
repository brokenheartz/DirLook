import requests as send
import re as regex
from random import choice
from datetime import datetime
from package.color import Color
from package.additional import remove_newline
from threading import Thread

# Coded By br0k3nh34rtz
# Thanks For Allah, Google, Youtube, and All Indonesian Hackers.
# Free to Recode and Share

class dirLook( Thread, Color ):

	__timeout  = 5
	__notfound = ["404", "not found", "tidak ditemukan", "tidak dikenal"]
	__agents = list(map(remove_newline, open("txt/user-agents.txt").readlines()))

	def __init__(self, target, dir, random_agent = False):
		Thread.__init__(self)
		self.url = target
		self.dir = dir
		self.rag = random_agent # rag's stand for Random Agent

	def checkPage(self, source_code):	# Check whether the status code suits the page
		for word in self.__notfound:
			if regex.compile(r'%s' % word, regex.IGNORECASE).search(source_code):
				return True
				break
			else:
				return False
				break

	def displayTime(self): # Displayed time
		time = datetime.now()
		hour = time.hour
		second = time.second
		minute = time.minute
		return "%d:%d:%d" % (hour, minute, second)

	def doingScanning(self): # Main method of this program
		try:
			if self.rag:
				agents = {"User-Agent" : choice(self.__agents).strip()}
				rikues = send.get(self.url + self.dir, timeout = self.__timeout, headers = agents) # We use GET method
			else:
				rikues = send.get(self.url + self.dir, timeout = self.__timeout) # We use GET method

			check = self.checkPage(rikues.text)
			
			# Coloring output
			if rikues.status_code == 200:
				color = self.BOLD + self.GREEN
			elif rikues.status_code == 403:
				color = self.BOLD + self.YELLOW
			elif rikues.status_code == 500:
				color = self.BOLD + self.BLUE
			elif rikues.status_code == 400:
				color = self.BOLD + self.MAGENTA
			else:
				color = self.BOLD + self.RED

			# Displaying output
			if rikues.status_code != 404:
				if rikues.status_code == 200 and check == True:
					print(color + "[%s] %s ::> %d ( Fake )" % (self.displayTime(), self.url + self.dir, rikues.status_code))
				else:
					print(color + "[%s] %s ::> %d" % (self.displayTime(), self.url + self.dir, rikues.status_code))
			else:
				pass
		except Exception:
			pass

	def run(self):
		self.doingScanning()

if __name__ == "__main__":
	print("Not main program, just a group of module.")
