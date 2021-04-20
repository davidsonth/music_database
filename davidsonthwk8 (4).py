#!/usr/bin/env python
# -*- coding: utf-8 -*-


# %% Simple selector (MySQL database)
# import pymysql for a simple interface to a MySQL DB

import pymysql

username1 = input("Username: ")
password1 = input("Password: ")


cnx = pymysql.connect(host='localhost', user=username1, password=password1, db='lotrfinal_1', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


cur = cnx.cursor()
stmt_select = "select character_name from lotr_character"
cur.execute(stmt_select)

rows = cur.fetchall()
count = 0
while (count == 0): 
	for row in rows:
		print(row["character_name"])
	cur.close()
	input_arg = input("Character Name: ")
	c3 = cnx.cursor()
	c3.callproc("track_character", [input_arg])
	for row in c3.fetchall():
		print(row)
	if c3.rowcount > 0:
		count = 1
	else:
	    print("bad input")
	
cur.close()

cnx.close()

	



