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
	time.sleep(0.6)
	print("\n\n[!] Requirement Library Is Not Installed...")
	print("[!] Connect To The Internet...")
	print("[!] Downloading Library...")
	os.system("pip install pillow")
	print("\n[!] Download Compleated, Installing Library...")
	time.sleep(0.5)
	print("[!] Process Compleated, Starting Tool..")
	time.sleep(1.5)
	os.system("python ToxLogo.py")

if not os.path.exists("/sdcard/Ascii_Logo"):
	os.system("mkdir /sdcard/Ascii_Logo")

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)

def logopsb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)

def logout():
    time.sleep(0.5)
    psb("\n\033[92m    [💓] Thanks For Using Our Tool..")
    psb("    [💓] For More Tools, Visit...")
    print("\n\t[ https://github.com/Toxic-Noob/ ]\n")
    sys.exit()


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
	with open(output_file+".txt", "w") as f:
		f.write(ascii_image)
	
	
def image_to_ascii_art_transparent(imgpath: str, output_file: str) -> str:
	image_path = imgpath
	img = Image.open(image_path)
	width, height = img.size
	aspect_ratio = height / width
	new_width = 65
	new_height = aspect_ratio * new_width * 0.55
	img = img.resize((new_width, int(new_height)))
	img = img.convert('L')
	pixels = img.getdata()
	chars = [" ", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
	new_pixels = [chars[pixel // 25] for pixel in pixels]
	new_pixels = ''.join(new_pixels)
	new_pixels_count = len(new_pixels)
	ascii_image = [new_pixels[index:index + new_width]
	for index in range(0, new_pixels_count, new_width)]
	ascii_image = "\n".join(ascii_image)
	with open(output_file+".txt", "w") as f:
		f.write(ascii_image)

def logo():
    print("\033[0;92m")
    os.system("clear")
    time.sleep(0.6)
    logopsb("    _             _ _       _                      \n   / \   ___  ___(_|_)     | |    ___   __ _  ___  \n  / _ \ / __|/ __| | |_____| |   / _ \ / _` |/ _ \ \n / ___ \\\__ \ (__| | |_____| |__| (_) | (_| | (_) |\n/_/   \_\___/\___|_|_|     |_____\___/ \__, |\___/ \n                                       |___/       \n")
    logopsb("\033[3;90m			   A Product Of ToxicNoob\033[0;92m")
    time.sleep(0.6)
    logopsb("\033[34m\n|****************************************************|\n|\033[3m Author   : HunterSl4d3                             \033[0;34m|\n|\033[3m Tool     : Ascii Logo                              \033[0;34m|\n|\033[3m Version  : 2.1                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : HunterSl4d3      		     	     \033[0;34m|\n******************************************************")
    time.sleep(0.8)


def img_ascii():
    op = options.op
    path_of_logo = input("\n\033[92m    [*] Enter Photo Path:> \033[37m")
    while not os.path.exists(path_of_logo):
    	psb("\n\033[91m    [!] File Path Dose Not Exists..\033[92m")
    	psb("    [!] Please Check Your File Path And Try Again...")
    	time.sleep(1)
    	path_of_logo = input("\n\033[92m    [*] Enter Photo Path:> \033[37m")
    path_out = input("\033[92m\n    [*] Enter Output file Name:> \033[37m").replace(".txt", "")
    if (op=="1"):
        image_to_ascii_art(path_of_logo, "/sdcard/Ascii_Logo/"+path_out)
    elif (op=="2"):
        path_out = path_out+"_trans"
        image_to_ascii_art_transparent(path_of_logo, "/sdcard/Ascii_Logo/"+path_out)

    psb("\033[92m\n    [*] Your Ascii Logo Saved in /sdcard/Ascii_Logo Directory as "+path_out+".txt..\n")
    time.sleep(0.5)
    play = input("    [!] Do You Want to Print Your Logo Now? [y/n]: ").lower()
    if(play=="") or (play=="y"):
    	psb("\n    [!] Decrease Your Screen Size to Get Perfect View Of Your Logo...\n")
    	time.sleep(0.3)
    	psb("\n    [❤️] Have a Nice Day!!\n\033[0;40;37m")
    	time.sleep(0.8)
    	os.system("cat /sdcard/Ascii_Logo/"+path_out+".txt")
    	print("\n")
    else:
        logout()


def options():
    psb("\n\033[92m    [*] Please Select an Option...")
    print("\n\033[92m    [01] Full Image")
    print("    [02] Transparent Image (Remove Background)")
    print("    [03] Exit")
    
    op = input("\n    [*] Enter Your Choice:> ").replace("0", "")
    while not (op=="1") and not (op=="2") and not (op=="3"):
        psb("\n    \033[91m[!] Choose an Option From Above..!!\033[92m")
        op = input("\n    [*] Enter Your Choice:> ").replace("0", "")
    if (op == "3"):
        logout()
    options.op = op
    img_ascii()


if __name__=='__main__':
    logo()
    options()
