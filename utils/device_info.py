import subprocess
import re
from typing import Dict, Any


def get_device_info():
    device = subprocess.run(['adb', 'shell', 'getprop'], capture_output=True, text=True)
    my_target = ['ro.product.build.version.release', 'ro.product.product.name']  # corresponding to device property list
    new_key = ['platformVersion', 'deviceName']  # corresponding to appium capability
    device_info: Dict[str, Any] = {}
    regx = r'\[|\]'

    if device.returncode == 0:
        info = device.stdout.strip().split('\n')

        for line in info:
            try:
                key, value = line.split(':', 1)
                key = re.sub(regx, '', key.strip())
                value = re.sub(regx, '', value.strip())

                if key in my_target:
                    device_info[new_key[my_target.index(key)]] = value
            except ValueError:
                continue

        return device_info
    elif device.returncode == 1:
        raise Exception("No devices/emulators found.")
    else:
        raise Exception("Error retrieving device information.")


def print_info():
    info_list = get_device_info()

    print('List of property')

    for key, value in info_list.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    print_info()
