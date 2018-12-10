import subprocess
import re

def get_data_space():
    command = 'adb shell df'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out = p.communicate()[0]
    size, used, free = re.findall(r'/data\s+(\d+\.\d+)\w\s+(\d+\.\d+)\w\s+(\d+\.\d+)\w', str(out))[0]
    # size, userd, free = re.findall(r'/data                    (\d+\.\d+)G    (\d+\.\d+)G    (\d+\.\d+)G', str(out))[0]
    return size, used, free

if __name__ == '__main__':
    size, userd, free = get_data_space()
    print("size: " + size + '\nused: ' + userd + '\nfree: ' + free)
    sizeInt=float(size)
    print(sizeInt)

