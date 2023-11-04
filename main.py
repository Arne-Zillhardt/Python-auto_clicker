'''import time

import pyautogui
pyautogui.FAILSAFE = False
from pynput import keyboard

# Initialize a variable to keep track of whether the Alt key is being pressed
alt_pressed = False
end = False

def on_press(key):
   global alt_pressed
   global end
   if key == keyboard.Key.shift:
       end = True

   if key == keyboard.Key.alt:
       alt_pressed = True

def on_release(key):
   global alt_pressed
   if key == keyboard.Key.alt:
       alt_pressed = False

# Start the keyboard listener
time.sleep(5)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
   while True:
       if end:
           break

       if not alt_pressed:
           # Execute your code here
           pyautogui.click()'''
from pynput import keyboard, mouse
import time

from pynput.mouse import Button, Controller

mouse = Controller()
# Initialize a variable to keep track of whether the auto clicker is active
auto_clicker_active = True

def click_mouse(button, sleep):
   mouse.click(button)
   time.sleep(sleep)

def on_press(key):
  global auto_clicker_active
  if key == keyboard.Key.alt: # Change this to the key you want to use to disable the auto clicker
      auto_clicker_active = False

def on_release(key):
  global auto_clicker_active
  if key == keyboard.Key.alt: # Change this to the key you want to use to disable the auto clicker
      auto_clicker_active = True

time.sleep(5)
# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  while auto_clicker_active:
      click_mouse(Button.left, 0.009)