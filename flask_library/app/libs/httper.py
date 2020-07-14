# -*- coding: utf-8 -*-
import requests

class Http:

    @staticmethod
    def get(url,return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text