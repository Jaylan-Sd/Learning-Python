import platform
import os

#os information

print(f"Os is : {platform.system()} {platform.system}")
print(f"Machine {platform.machine()}")

print(platform.freedesktop_os_release())

print(os.getlogin())
print(os.cpu_count())
