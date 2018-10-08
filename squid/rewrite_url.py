#!/usr/bin/env python3

import sys


def main():
    """
        keep looping and processing requests
        request format is based on url_rewrite_extras "%>a %>rm %un"
    """
    request = sys.stdin.readline()
    ch_id, url, ipaddr, method, user = request.split()
    response = ch_id + ' OK'
    response += ' rewrite-url=https://httpbin.org/ip'
    response += '\n'
    sys.stdout.write(response)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
