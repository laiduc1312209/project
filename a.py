import wmi

def get_hwid():
    c = wmi.WMI()
    hwid = []

    for item in c.Win32_ComputerSystemProduct():
        hwid.append(item.UUID)

    return hwid

if __name__ == "__main__":
    hwid = get_hwid()
    print("Hardware ID(s):", hwid)
