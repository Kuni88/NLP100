#coding: utf-8
#NLP100
#http://www.cl.ecei.tohoku.ac.jp/nlp100/

import sys
import json
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

#read file
file = 'jawiki-country.json'
f = open(file, 'r')

#イギリスが出るまでfileを読み続ける
while True:
    str_f = f.readline()
    if str_f=="":
        break
    jsondata = json.loads(str_f)
    if jsondata['title']==u'イギリス':
        #text部分を書き出す
        print jsondata['text']
        break


