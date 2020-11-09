#!/usr/bin/python
"""tweet module for ansible
 Copyright: (c) 2020, Daisuke Matsui <dmatsui@redhat.com>
"""

import http.client
from plugins.modules.twitter_tweet import tweet
from unittest.mock import Mock, patch


@patch('urllib.request.urlopen', autospec=True)
def mocked_tweet(mocked_urlopen):
    """test method
    """
    mocked_headers = http.client.HTTPMessage()
    mocked_headers._headers = [
        ('cache-control', 'no-cache, no-store, must-revalidate, pre-check=0, post-check=0'),
        ('connection', 'close'),
        ('content-disposition', 'attachment; filename=json.json'),
        ('content-length', 'XXXX'),
        ('content-type', 'application/json;charset=utf-8'),
        ('date', 'Mon, 05 Oct 2020 11:34:33 GMT'),
        ('expires', 'Tue, 31 Mar 1981 05:00:00 GMT'),
        ('last-modified', 'Mon, 05 Oct 2020 11:34:32 GMT'),
        ('pragma', 'no-cache'),
        ('server', 'tsa_m'),
        ('set-cookie', 'personalization_id="v1_9JKLYs/rmnzpKEFJVfZadQ=="; Max-Age=63072000; Expires=Wed, 05 Oct 2022 11:34:32 GMT; Path=/; Domain=.twitter.com; Secure; SameSite=None'),
        ('set-cookie', 'lang=ja; Path=/'),
        ('set-cookie', 'guest_id=v1%3A160189767240567023; Max-Age=63072000; Expires=Wed, 05 Oct 2022 11:34:32 GMT; Path=/; Domain=.twitter.com; Secure; SameSite=None'),
        ('status', '200 OK'),
        ('strict-transport-security', 'max-age=631138519'),
        ('x-access-level', 'read-write'),
        ('x-connection-hash', 'XXX'),
        ('x-content-type-options', 'nosniff'),
        ('x-frame-options', 'SAMEORIGIN'),
        ('x-response-time', 'XXX'),
        ('x-transaction', 'XXX'),
        ('x-tsa-request-body-time', '0'),
        ('x-twitter-response-tags', 'BouncerCompliant'),
        ('x-xss-protection', '0')
    ]
    mocked_headers._payload = ''
    mocked_urlopen.return_value.fp = None
    mocked_urlopen.return_value.debuglevel = 0
    mocked_urlopen.return_value._method = 'POST'
    mocked_urlopen.return_value.headers = mocked_headers
    mocked_urlopen.return_value.msg = 'OK'
    mocked_urlopen.return_value.version = 11
    mocked_urlopen.return_value.status = 200
    mocked_urlopen.return_value.reason = 'OK'
    mocked_urlopen.return_value.chunked = False
    mocked_urlopen.return_value.chunk_left = 'UNKNOWN'
    mocked_urlopen.return_value.length = 0
    mocked_urlopen.return_value.will_close = True
    mocked_urlopen.return_value.code = 200
    mocked_urlopen.return_value.url = 'https://api.twitter.com/1.1/statuses/update.json'

    tweet()


def main():
    """call mocked method
    """
    mocked_tweet()


if __name__ == '__main__':
    main()
