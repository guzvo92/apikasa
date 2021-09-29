import sqlite3

class Maindb:

    def __init__(self,dbfile):
        #self son para propiedades de la clase (variables)
        try:
            self.conexion = sqlite3.connect(dbfile) #me genera file si no existe
            self.cursor = self.conexion.cursor() #Ejecutar consultas
            print("Conexion creada") #el cursor me genera objetos          
        except:
            print("no se creo la db")

    def desco(self):
        self.conexion.close()

    def borrartabla(self,tabla):
        v1="DROP TABLE "
        v2= tabla
        v3= " "
        value = v1+v2+v3
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def creartabla(self,tabla):
        v1="CREATE TABLE IF NOT EXISTS "
        v2= tabla
        v3= "( id INTEGER PRIMARY KEY AUTOINCREMENT,"
        v4 ="rankv1 int(255),"
        v5 ="namev2 varchar(255),"
        v6 ="pricev3 int(255),"
        v7 ="mcapv4 int(255),"
        v8 ="supplyv5 int(255),"
        v9 ="percent1dv6 int(255),"
        v10 ="percent7dv7 int(255),"
        v11 ="percent30dv8 int(255)"
        v12 = " )"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12
        print(value)
        self.cursor.execute(value)
        self.conexion.commit()

    def insertnewdata(self,tabla,m1,m2,m3,m4,m5,m6,m7,m8):
        v1 = "INSERT INTO "
        v2 = tabla
        v3 = " VALUES (null, '"
        v4 = m1
        v5 = "','"
        v6 = m2
        v7 = "','"
        v8 = m3
        v9 = "','"
        v10= m4
        v11 = "','"
        v12= m5
        v13 = "','"
        v14 = m6
        v15 = "','"
        v16= m7
        v17 = "','"
        v18= m8
        v19 = "')"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    #editar a parametros opcionales PENDIENTE
    def updatevalfull(self,circuito,valor,stringon,stringoff):
        a1 = "UPDATE circuitos "
        a2 = "SET estado = "
        a3 = valor
        a4 = ","
        a5 = "stringon = '"
        a6 = stringon
        a7 = "'"
        a8 = ","
        a9 = "stringoff = '"
        a10 = stringoff
        a11 = "' WHERE titulo= '"
        a12 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12
        value2 = a1+a2+a3+a11+a12
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def updateval(self,circuito,valor):
        a1 = "UPDATE circuitos "
        a2 = "SET estado = "
        a3 = valor
        a4 = " WHERE titulo= '"
        a5 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def updatestrings(self,circuito,stringon,stringoff):
        a1 = "UPDATE circuitos "
        a2 = "SET stringon = '"
        a3 = stringon
        a4 = "'"
        a5 = ","
        a6 = "stringoff = '"
        a7 = stringoff
        a8 = "' WHERE titulo= '"
        a9 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5+a6+a7+a8+a9
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def deleteval(self,id):
        v1 = "DELETE FROM circuitos WHERE id="
        v2 = str(id) + " "
        value= v1+v2
        #print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def readallcircuitos(self):
        self.cursor.execute("SELECT * FROM circuitos")
        self.circuitos = self.cursor.fetchall()
        #print(self.circuitos)
        self.conexion.commit()
        return self.circuitos

    def readallmaindata(self):
        self.cursor.execute("SELECT * FROM admin")
        self.admindb = self.cursor.fetchall()
        #print(self.circuitos)
        self.conexion.commit()
        return self.admindb



