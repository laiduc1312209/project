# import wmi

# def get_hwid():
#     c = wmi.WMI()
#     hwid = []

#     for item in c.Win32_ComputerSystemProduct():
#         hwid.append(item.UUID)

#     return hwid

# if __name__ == "__main__":
#     hwid = get_hwid()
#     print("Hardware ID(s):", hwid)

import requests

def load_string_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        return response.text
    except requests.RequestException as e:
        print(f"Lỗi khi tải dữ liệu từ URL: {e}")
        return None

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/laiduc1312209/project/main/python"
    data = load_string_from_url(url)
    if data is not None:
        print("Nội dung tải về:")
        print(data)

