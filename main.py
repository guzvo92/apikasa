#Linkserv main.py
production = 1

from flask import Flask
app = Flask(__name__) #peso1

from views import * #[peso2] Archivo de rutas Maestro


#Code ISOLATED
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

mip = get_ip()

#tiene que ir al final de las rutas NOTA!
#//si corro archivo llamado "main" -> palabra reservada
#//que se ejecute en modo debug

if __name__ == '__main__':
    if production == 1:
        app.run(debug=False,host =str(mip),port=2600)
    else:
        app.run(debug=True,port=2600)