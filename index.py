import serial
import mysql.connector
import datetime

#Konfigurasi koneksi serial arduino
arduino = serial.Serial("/dev/cu.usbserial-1410", 115200)

#Konfigurasi koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dataMonitoring"
)

#perintah insert data ke dalam tabel database
def mysqlInsert(data1, data2, data3, data4, data5, data6, data7, data8):
    cursor = db.cursor()
    sql = "INSERT INTO solarcell (time, teganganPV, arusPV, dayaPV, teganganPLN, arusPLN, dayaPLN, suhu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (data1, data2, data3, data4, data5, data6, data7, data8)
    cursor.execute(sql, val)
    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

#infinity loop untuk kirim data ke database
while True:
    x = datetime.datetime.now()
    time = x.strftime("%X")
    data = arduino.readline().decode("utf-8")
    simpanData = data.split(", ")
    print(simpanData)
    mysqlInsert(time,simpanData[0],simpanData[1],simpanData[2],simpanData[3],simpanData[4],simpanData[5],simpanData[6])