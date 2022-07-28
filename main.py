#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:17:31 2022

@author: amir
"""
from youtube import get_user_url, get_link_file, get_user_choice


def run():
    url = get_user_url()
    link = get_link_file(url)
    get_user_choice(link)


if __name__ == '__main__':
    run()
