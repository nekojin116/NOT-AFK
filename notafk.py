from pynput.keyboard import Key, Controller
import time



keyboard = Controller()

print('Hello, world!')
print('This is a simple script that imitiates in-game mouvements')
print('To prevent getting kicked for begin afk by the game')
print('Code made by nekojin116 , im not responsible for any bans')
print('Code will start running after 5s')
time.sleep(5)



for i in range(1,100):
   keyboard.press('w')
   keyboard.release('w')
   keyboard.press('s')
   keyboard.release('s')
   keyboard.press(Key.space)
   keyboard.release(Key.space)
   time.sleep(5)
   
