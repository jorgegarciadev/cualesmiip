#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, re

def validator(userUrl):
    # http://regex101.com/r/pB0rD4
    pattern = '(http://)?(((www\.)?(\w+\.)+([a-z]{2,6}))|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))'
    matched = re.match(pattern, userUrl, re.IGNORECASE)

    if matched:
        url = matched.group(0)
        scheme = matched.group(1)
        host = matched.group(2)
    else:
        return None
    # path is ignored
    if not scheme:
        url = 'http://' + host
        scheme = 'http://'

    return (url, scheme, host)


def pokeSite(host, path = "/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        statusCode = conn.getresponse().status
        response = httplib.responses[statusCode]

        return {'code': statusCode, 'response':response}
    
    except StandardError:
        return None

def answer(userUrl):
    parsedUrl = validator(userUrl)
    if parsedUrl == None:
        return u"Err... No me viene nada por %s ¿Pruebo con Fernández?" % (userUrl)
    else:
        host = parsedUrl[2]
        response = pokeSite(host)

    if response == None or response['code'] >= 400:
        return u"Efectivamente, %s está caido" % (userUrl)
    else:
        return u"Parece que sólo eres tú. Desde aquí se puede acceder a %s" % (userUrl)
