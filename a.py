import requests

def load_and_run_code_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        code = response.text
        exec(code)  # Thực thi mã đã tải
    except requests.RequestException as e:
        print(f"Lỗi khi tải dữ liệu từ URL: {e}")
    except Exception as e:
        print(f"Lỗi khi thực thi mã: {e}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/laiduc1312209/project/main/a.py"
    load_and_run_code_from_url(url)
