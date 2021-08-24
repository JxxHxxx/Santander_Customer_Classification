import scipy.io
import csv
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='111111', db='santander', charset='utf8')
conn.cursor()
conn.commit()

f = open('C:/Users/JH/Desktop/Santander Customer Transaction Prediction/test.csv','r')

csvReader = csv.reader(f)

conn.commit()

f.close()
conn.close()