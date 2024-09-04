import requests as req

def request(url):
    try:
        response = req.get(url)
        if response.status_code == 200:
            return response.text
    except req.RequestException as e:
        print(e)
        return None

def main():
    url = "https://prodev.jd.com/mall/active/31XPWPTonxJ9e5YoQ85HS7z8XNYQ/index.html?babelChannel=ttt40"
    html = request(url)
    print(html)

if __name__ == "__main__":
    main()