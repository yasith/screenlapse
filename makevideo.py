#! /usr/bin/env python3
import getopt
import os
import os.path
import subprocess
import sys

PREFIX = "screen"
HELP_STR = "makevideo.py -o <outputdir> -f <movie_file_name>"
PIXEL_FORMAT = "yuv420p"

def main():
	fdir, filename = get_args()
	screen = PREFIX + "%10d.png"

	print(os.path.expanduser(fdir))
	os.chdir(os.path.expanduser(fdir))
	subprocess.call(["ffmpeg", "-r", "24", "-y", "-i", screen, "-b", "15000k", "-pix_fmt", PIXEL_FORMAT, filename])

def get_args():
	fdir = "~/screencaps"       
	filename = "timelapse.m4v"

	argv = sys.argv[1:]
	try:
		opts, args = getopt.getopt(argv,"ho:f:", ["out=", "help", "file="])
	except getopt.GetoptError:
		print(HELP_STR)
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print(HELP_STR)
			sys.exit(0)
		elif opt in ("-o", "--out"):
			fdir = arg
		elif opt in ("-f", "--file"):
			filename = arg

	return fdir, filename

if __name__ == '__main__':
	main()