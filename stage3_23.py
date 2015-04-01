#coding: utf-8                                                                  

f = open('uk_content.txt', 'r')

for line in f.readlines():
    if '==' in line:
        line = line.strip()
        section = line.replace('=', '').strip()
        section_level = (len(line) - len(section))/2 - 1
        print ' '*section_level+section, section_level
f.close()
