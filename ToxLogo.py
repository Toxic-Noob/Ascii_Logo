#!/usr/bin/python3
#######################################
# Coded By HunterSl4d3
# A Product Of ToxicNoob
# https://github.com/Toxic-Noob/
# Don't Try to Copy Any Codes
# Taking Creadits of Others Code,
# Will Not Make You A Coder
######################################



import os
import sys
import time
try:
	from PIL import Image
except:
	print("\n\n[!] Requirement Library Is Not Installed...")
	print("[!] Connect To The Internet...")
	print("[!] Downloading Library...")
	os.system("pip install pillow")
	print("\n[!] Download Compleated, Installing Library...")
	print("[!] Process Compleated, Starting Tool..")
	time.sleep(1.5)
	os.system("python ToxLogo.py")

if not os.path.exists("/sdcard/Ascii_Logo"):
	os.system("mkdir /sdcard/Ascii_Logo")

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.003)

def image_to_ascii_art(imgpath: str, output_file: str) -> str:
	image_path = imgpath
	img = Image.open(image_path)
	width, height = img.size
	aspect_ratio = height / width
	new_width = 80
	new_height = aspect_ratio * new_width * 0.55
	img = img.resize((new_width, int(new_height)))
	img = img.convert('L')
	pixels = img.getdata()
	chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
	new_pixels = [chars[pixel // 25] for pixel in pixels]
	new_pixels = ''.join(new_pixels)
	new_pixels_count = len(new_pixels)
	ascii_image = [new_pixels[index:index + new_width]
	for index in range(0, new_pixels_count, new_width)]
	ascii_image = "\n".join(ascii_image)
	with open(f"{output_file}.txt", "w") as f:
		f.write(ascii_image)
	return ascii_image

print("\033[0;92m")
os.system("clear")
time.sleep(0.6)
logopsb("    _             _ _       _                      \n   / \   ___  ___(_|_)     | |    ___   __ _  ___  \n  / _ \ / __|/ __| | |_____| |   / _ \ / _` |/ _ \ \n / ___ \\\__ \ (__| | |_____| |__| (_) | (_| | (_) |\n/_/   \_\___/\___|_|_|     |_____\___/ \__, |\___/ \n                                       |___/       \n")
logopsb("\033[3;90m			   A Product Of ToxicNoob\033[0;92m")
time.sleep(0.6)
logopsb("\033[34m\n|****************************************************|\n|\033[3m Author   : HunterSl4d3                             \033[0;34m|\n|\033[3m Tool     : Ascii Logo                              \033[0;34m|\n|\033[3m Version  : 1.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : HunterSl4d3      		     	     \033[0;34m|\n******************************************************")
time.sleep(0.8)

path_of_logo = input("\n\033[92;3m[*] Enter Photo Path:> ")
if not os.path.exists(path_of_logo):
	psb("\n\033[31m[!] File Path Dose Not Exists..")
	psb("[!] Please Check Your File Path And Try Again...")
	time.sleep(1.5)
	os.system("python ascii_art.py")
path_out = input("\n[*] Enter Output file Name:> ")
psb("\n[*] Please Wait...")

image_to_ascii_art(path_of_logo, "/sdcard/Ascii_Logo/"+path_out)

psb("\n[*] Your Ascii Logo Saved in /sdcard/Ascii_Logo Directory..\n")
time.sleep(0.9)
play = input("[!] Do You Want to Print Your Logo Now?[y/n]: ").lower()
if(play==""):
	psb("\n[!] Decrease Your Screen Size to Get Perfect View Of Your Logo\n")
	time.sleep(0.3)
	psb("\n[❤️] Have a Nice Day!!\n\033[0;40;37m")
	time.sleep(0.8)
	os.system("cat /sdcard/Ascii_Logo/"+path_out+".txt")
elif(play=="y"):
	psb("\n[!] Decrise Your Screen Size To Get Perfect View Of Your Logo\n")
	time.sleep(0.3)
	psb("\n[❤️] Have a Nice Day!!\n\033[0;40;37m")
	time.sleep(0.8)
	os.system("cat /sdcard/Ascii_Logo/"+path_out+".txt")
else:
	psb("\n[❤️] Have a Nice Day!!\n\033[0;40;37m")
