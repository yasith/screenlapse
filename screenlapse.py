import subprocess
import time
import os

def main():
	i = 0
	prefix = "screen"
	fdir = "~/screencaps"

	if not os.path.exists(os.path.expanduser(fdir)):
		os.mkdir(os.path.expanduser(fdir))

	while 1:
		fname = prefix + str(i).zfill(10) + ".png"
		fpath = os.path.expanduser(os.path.join(fdir, fname))
		if not os.path.exists(fpath):
			break
		i += 1

	while 1:
		fname = prefix + str(i).zfill(10) + ".png"
		fpath = os.path.expanduser(os.path.join(fdir, fname))
		print(fpath)
		subprocess.call(["screencapture", "-t", "png", "-x", fpath])
		time.sleep(1)
		print(fname)
		i += 1


if __name__ == "__main__":
	main()