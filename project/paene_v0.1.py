#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 
#  
#  Copyright 2018 Oliver, Nicolas & Lauri
#  
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="dbuser",
        passwd="dbpass",
        db="theverge",
        buffered=True)


# # #  [FUNCTIONS] # # #




# # # [MAIN PROGRAM] # # #

lauri = 2
was = 5
here = 1337










db.rollback()
