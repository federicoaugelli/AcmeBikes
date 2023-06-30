import subprocess, platform

path = "../camunda/"

current_platform = platform.system()


if current_platform == "Windows":
    proc = subprocess.Popen([path + "start.bat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

else:
    proc = subprocess.Popen([path + "start.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

input("type something to exit the program...")

if current_platform == "Windows":
    subprocess.run(path + "shutdown.bat")

else:
    subprocess.run(path + "shutdown.sh")


