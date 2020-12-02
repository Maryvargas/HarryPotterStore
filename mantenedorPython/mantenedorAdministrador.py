import pymysql 

import claseAdministrador 

def conectar():
    try:
       conexion = pymysql.connect(host='localhost',
                                   user= 'root',
                                   password='',
                                   db='patronusstore')
    except:
       print("Error de conexion")
    return conexion

    
#Programa principal
conectar()
print("Conectado")   


def selectTest():
    #To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='patronusstore'
        )

    cur = conn.cursor()
    cur.execute("SELECT * FROM producto")
    output = cur.fetchall()

    return output

def insertarTest(nombre_usuario):
    #To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='patronusstore'
        )

    cur = conn.cursor()
    sql = "INSERT INTO usuario (nombre_usuario) VALUES (%s)"
    cur.execute(sql, nombre_usuario)
    conn.commit()

    conn.close()


def selectTest():
    #To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='patronusstore'
        )

    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario")
    output = cur.fetchall()

    return output


def updateTest(nombre_usuario, nuevo):
    #To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='patronusstore'
        )

    cur = conn.cursor()
    sql = "UPDATE usuario SET nombre_usuario = %s WHERE nombre_usuario = %s"
    val = (nuevo, nombre_usuario)
    cur.execute(sql, val)
    conn.commit()

    conn.close()


def deleteTest(id):
    #To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='patronusstore'
        )

    cur = conn.cursor()
    sql = "DELETE FROM usuario WHERE nombre_usuario = %s"
    cur.execute(sql, nombre_usuario)
    conn.commit()

    conn.close()
