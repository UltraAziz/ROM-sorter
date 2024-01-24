import os, pathlib, shutil, time, sys
from pathlib import Path

directory = False
text = "Sorting will start in "
def create_directory(console):
      path = fr'./{console}'
      directory = os.path.isdir(path)
      if directory == False:
       path = "./"
       os.mkdir (fr"./{console}")
      
def sort_files(rom, console):
  if file.endswith(rom):
   create_directory(console)
   path = './'
   shutil.move(fr'./{file}', fr'./{console}/{file}')
   print(fr"Found {console} ROM: " + file)


print("This script will automatically arange your ROM files into folders for each console.")
print(".iso files cannot be sorted due to all disc based consoles using them.")
print(".zip files are assumed to be Arcade archives.") 
print(text + "5 Seconds", end='\r')
time.sleep(1)
print(text + "5 Seconds", end='\r')
time.sleep(1)
print(text + "4 Seconds", end='\r')
time.sleep(1)
print(text + "3 Seconds", end='\r')
time.sleep(1)
print(text + "2 Seconds", end='\r')
time.sleep(1)
print(text + "1 Seconds", end='\r')
time.sleep(1)


for file in os.listdir ("./"):
 sort_files(".nes", "NES")
 sort_files(".sfc", "SNES")
 sort_files(".smc", "SNES")
 sort_files(".bin", "Sega Genesis")
 sort_files(".gen", "Sega Genesis")
 sort_files(".smd", "Sega Mega Drive")
 sort_files(".sms", "Sega Master System")
 sort_files(".v64", "Nintendo 64")
 sort_files(".z64", "Nintendo 64")
 sort_files(".n64", "Nintendo 64")
 sort_files(".gb", "Game Boy")
 sort_files(".gbc", "Game Boy Color")
 sort_files(".gba", "Game Boy Advance")
 sort_files(".32x", "Sega 32X")
 sort_files(".68k", "SEGA Mega Drive & Genesis Classics")
 sort_files(".iso", "Disc Image")
 sort_files(".zip", "Arcade")
 sort_files(".gg", "Sega Game Gear")
 sort_files(".ds", "Nintendo DS")
 sort_files(".nds", "Nintendo DS")
 sort_files(".dsi", "Nintendo DSiware")
 sort_files(".3ds", "Nintendo 3ds")
 sort_files(".cia", "Nintendo 3DS CIA")
