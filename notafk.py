from pynput.keyboard import Key, Controller
import time
from colorama import Fore, Back, Style


keyboard = Controller()

print(Fore.RED +'Made by nekojin116   script will start running after 5s , it will press w , s and space then repeat every 5sec  not responsible for any bans in game resulted due to this script')
time.sleep(5)

for i in range(1,100):
   keyboard.press('w')
   keyboard.release('w')
   keyboard.press('s')
   keyboard.release('s')
   keyboard.press(Key.space)
   keyboard.release(Key.space)
   time.sleep(5)
   
