import subprocess, platform, signal, os

path = "../camunda/"

current_platform = platform.system()


if current_platform == "Windows":
    proc = subprocess.Popen([path + "start.bat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

else:
    proc = subprocess.Popen([path + "start.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

bank = subprocess.Popen(["uvicorn", "main:app", "--reload"], cwd="../bank")
courier = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8001"], cwd="../courier")
geoloc = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8002"], cwd="../geoloc")

input("type something to exit the program...")

if current_platform == "Windows":
    subprocess.run(path + "shutdown.bat")

else:
    subprocess.run(path + "shutdown.sh")

os.killpg(os.getpgid(bank.pid), signal.SIGINT)
os.killpg(os.getpgid(courier.pid), signal.SIGINT)
os.killpg(os.getpgid(geoloc.pid), signal.SIGINT)

