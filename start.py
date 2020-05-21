#!/usr/bin/python
# -*- coding: utf-8 -*-
"""News @gpupo"""

import os
from newscatcher import Newscatcher, urls

from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def show_list(articles):
    for news in articles:
        print('* [{0}]({1})\n{2}\n'.format(news.title, news.link, strip_tags(news.summary)))
 
def show_news_from(domain):
    print('## {0} \n'.format(domain))
    source = Newscatcher(website = domain)
    results = source.get_news()
    show_list(results['articles'])

def main():
    print('# @gpupo news | index')
    show_news_from('news.ycombinator.com')
    show_news_from('nytimes.com')
    show_news_from('globo.com')
    
if __name__ == '__main__':
    main()
