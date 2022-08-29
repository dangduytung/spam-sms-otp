#!/usr/bin/env python
import requests
from log_base import log

"""
======================= MAIN
"""


def hello():
    print('hello')
    return "hello"


def requestSpamSmsOtp(sdt, url):
    log.info(f'sdt: {sdt}')
    log.info(f'url: {url}')
    url = url.replace('{sdt}', sdt)
    try:
        r = requests.post(url)
        r.raise_for_status()
        log.info(r.text)
        return True
    except requests.exceptions.HTTPError as errh:
        log.error(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        log.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        log.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        log.error(f"OOps: Something Else {err}")
    return False
