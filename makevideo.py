import subprocess
import os
import os.path

print(os.path.expanduser("~/screencaps"))
os.chdir(os.path.expanduser("~/screencaps"))
subprocess.call(["ffmpeg", "-r", "24", "-y", "-i", "screen%10d.png", "-b", "15000k", "-pix_fmt", "yuv420p", "timelapse.m4v"])