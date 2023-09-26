import subprocess, platform, signal, os

current_platform = platform.system()

if "Windows" in current_platform:
    path = "..\\camunda\\"
    proc = subprocess.Popen([path + "start.bat"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

else:
    path = "../camunda/"
    proc = subprocess.Popen([path + "start.sh"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

bank = subprocess.Popen(["uvicorn", "main:app", "--reload"], cwd="../backend/bank")
courier = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8001"], cwd="../backend/courier")
geoloc = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8002"], cwd="../backend/geoloc")
supplier = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8003"], cwd="../backend/supplier")
database = subprocess.Popen(["uvicorn", "main:app", "--reload", "--port", "8004"], cwd="../backend/acmeDB")

input("type enter to exit the program...")

if "Windows" in current_platform:
    subprocess.run(path + "shutdown.bat")

else:
    subprocess.run(path + "shutdown.sh")

os.killpg(os.getpgid(bank.pid), signal.SIGINT)
os.killpg(os.getpgid(courier.pid), signal.SIGINT)
os.killpg(os.getpgid(geoloc.pid), signal.SIGINT)
os.killpg(os.getpgid(supplier.pid), signal.SIGINT)
os.killpg(os.getpgid(database.pid), signal.SIGINT)

