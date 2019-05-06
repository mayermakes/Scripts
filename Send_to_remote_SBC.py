import os
print("FILESENDER by mayermakes CC-BY-SA 2019")
print(" this piece of Software comes as is without any warranty, it is potentially insecure, only use this if you know what your are doing. Happy hacking.")
print("___________________________________________________________________")
print("Please enter target:")
SBC = input("IP of receiving RPI: ")
USER = input("Username on remote SBC: ")
print("Sending Files to " + SBC)
os.system("scp -r /home/mayermakes/SENDFILES "+ USER +"@"+ SBC +":/home/pi/")
print("Files sent to " + SBC)


