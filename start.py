#!/usr/bin/python
# -*- coding: utf-8 -*-
"""News @gpupo"""

import os
from newscatcher import Newscatcher, urls
from datetime import datetime

def show_list(articles):
    for news in articles:
        print('* [{0}]({1})\n'.format(news.title, news.link))
 
def show_news_from(domain):
    print('## {0} \n\n'.format(domain))
    source = Newscatcher(website = domain)
    results = source.get_news()
    show_list(results['articles'])

def main():
    print("---\nlayout: default\n---\n")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('# indexed at {0} UTC\n\n'.format(dt_string))
    domains = ['news.ycombinator.com','nytimes.com' ,'globo.com']
    for d in domains:
        show_news_from(d)
    
if __name__ == '__main__':
    main()
