#!/usr/bin/python

import urllib, webbrowser, ConfigParser, os, unicodedata

def results(parsed, original_query):
    return {
        "title": 'Redmine search',
        "run_args": [parsed['~words']]
    }

def run(words):
    config = ConfigParser.SafeConfigParser()
    config.read('%s/.redmine' % os.environ['HOME'])
    baseurl = config.get('redmine', 'baseurl')
    normalized = unicodedata.normalize('NFC', words)
    encoded = urllib.quote_plus(normalized.encode('utf8'))
    url = '{0}/search?utf8=%E2%9C%93&q={1}'.format(baseurl, encoded)
    webbrowser.open_new_tab(url)
