class ParseHeader:

    @staticmethod
    def do_parse(lines) -> dict:
        headers = {}

        for line in lines:
            if line.startswith(':'):
                continue
            elif line.startswith('cookie'):
                continue
            else:
                kv = line.split(":")
                headers[kv[0]] = kv[1].strip()

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
