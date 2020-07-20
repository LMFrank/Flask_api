# -*- coding: utf-8 -*-
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4128.3 Safari/537.36'
}


class Http:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url, headers=headers, verify=False)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
