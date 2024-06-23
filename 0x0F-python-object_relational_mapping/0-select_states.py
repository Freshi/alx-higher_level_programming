#!/usr/bin/python3
'''
List all states fron the database `hbtn_0e_0_usd`
'''

import sys
import MySQLdb

db = MySQLdb.connect(host='localhost:3306', user=sys.argv[2], passwd=sys.argv[3], database=sys.argv[4])
cur = db.cursor()
data = cur.execute('SELECT * FROM states ORDER BY id')
[print x for x in data]
cur.close()
cur.close()
