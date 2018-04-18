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
        db="paene",
        buffered=True)


# # #  [FUNCTIONS] # # #




# # # [MAIN PROGRAM] # # #










db.rollback()
