#! /usr/bin/env python3
import getopt
import os
import subprocess
import sys
import time

HELP_STR = "screenlapse.py -o <outputdir> -t <time_interval>"
PREFIX = "screen"

def main():

	interval, fdir = get_args()
	print("Screenlapse interval:", interval)
	print("Screenlapse directory:", fdir)

	if not os.path.exists(os.path.expanduser(fdir)):
		os.mkdir(os.path.expanduser(fdir))

	frame = find_next(fdir)

	while 1:
		take_snap(fdir, interval, frame)
		frame += 1

def find_next(fdir):
	frame = 0

	fname = PREFIX + str(frame).zfill(10) + ".png"
	fpath = os.path.expanduser(os.path.join(fdir, fname))

	while os.path.exists(fpath):
		frame += 1
		fname = PREFIX + str(frame).zfill(10) + ".png"
		fpath = os.path.expanduser(os.path.join(fdir, fname))

	return frame

def get_args():
	interval = 1
	fdir = "~/screencaps"       

	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv,"ho:t:", ["out=","time=","help"])
	except getopt.GetoptError:
		print(HELP_STR)
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print(HELP_STR)
			sys.exit(0)
		elif opt in ("-o", "--out"):
			fdir = arg
		elif opt in ("-t", "--time"):
			arg.strip()
			interval = float(arg)

	return interval, fdir

def take_snap(fdir, interval, frame):

	fname = PREFIX + str(frame).zfill(10) + ".png"
	fpath = os.path.expanduser(os.path.join(fdir, fname))

	subprocess.call(["screencapture", "-t", "png", "-x", fpath])
	print(fpath)

	time.sleep(interval)


if __name__ == "__main__":
	main()
