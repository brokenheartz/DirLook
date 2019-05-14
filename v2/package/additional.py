from package.color import Color
import time, random, sys

color = Color()

# Coded By br0k3nh34rtz
# Thanks For Allah, Google, Youtube, and All Indonesian Hackers.
# Free to Recode and Share 

banner_text = color.YELLOW + """
 _____  _      _                 _
|  __ \(_)    | |               | |
| |  | |_ _ __| |     ___   ___ | | __
| |  | | | '__| |    / _ \ / _ \| |/ /
| |__| | | |  | |___| (_) | (_) |   <
|_____/|_|_|  |______\___/ \___/|_|\_\\
\t\t      [ Version 1.2 ]
"""

def banner():
	print(banner_text)

def usage():
	print(color.WHITE + "[!] Usage : ./dirlook.py --url <url> --wordlist <file/dir list>")
	print(color.WHITE + "[!] Help  : ./dirlook.py --help / -h")

def exit_loading():
	try:
		print(color.BOLD + color.YELLOW + "\n[-] Exiting Program", end = "")
		for count in range(0, random.randint(3,7)):
			sys.stdout.write(".")
			sys.stdout.flush()
			time.sleep(0.45)
		print()
	except(KeyboardInterrupt, SystemExit):
			pass
	sys.exit(0)

remove_newline = lambda x : x.replace("\n","")

if __name__ == "__main__":
	print("Not main program, just a group of module.")
