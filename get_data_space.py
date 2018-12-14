import subprocess
import re

def get_data_space():
    command = 'adb shell df'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    size, userd, free = re.findall(r'/data\s+(\d+\.\d+)G\s+(\d+\.\d+)G\s+(\d+\.\d+)G', str(out))[0]
    return size, userd, free

if __name__ == '__main__':
    size, userd, free = get_data_space()
    print("size: " + size + '\nused: ' + userd + '\nfree: ' + free)

