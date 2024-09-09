class ParseHeader:

    @staticmethod
    def do_parse(lines) -> dict:
        headers = {}

        for line in lines:
            if line.startswith('accept'):
                headers['accept'] = line.split(":")[1].strip()
            elif line.startswith('content-type'):
                headers['content-type'] = line.split(":")[1].strip()
            elif line.startswith('user-agent'):
                headers['user-agent'] = line.split(":")[1].strip()
            elif line.startswith('sec-ch-ua-platform'):
                headers['sec-ch-ua-platform'] = line.split(":")[1].strip()
            elif line.startswith('referer'):
                headers['referer'] = line.split(":")[1].strip()


        print('parse_header:')
        print(headers)
        return headers

    @staticmethod
    def do_parse_cookie(lines):
        cookies = {}

        for line in lines:
            if line.startswith('cookie'):
                cookie = line.split(":")[1].strip()
                cookie_info = cookie.split("=")
                cookies[cookie_info[0]] = cookie_info[1]

        print('cookie: ')
        print(cookies)
        return cookies
