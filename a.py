# -*- coding: utf-8 -*-
def log(text):
    file_object = open('thefile.txt', 'w+')
    file_object.write(text)
    file_object.write("\n\n")
    file_object.close( )

log("a")
