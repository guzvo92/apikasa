import os #para crear el salto de linea


#############################    funciones file makers  ########################################
#para una estructura de 50 registros

def Crearutas(items,methods,uri):
    #item = array
    #funct= array

    file = open(uri, "w") #crea archivo
    file.close()  #limpiando archivo

    import0 = "#//[This is an Autofile by GMAN]"
    import1 = "from main import app"
    import2 = "from app.agenservices.dbservice import *"
    import3 = "from app.services.mainlightservice import Mainobject,Mainstrip"

    file = open(uri, "a") #append
    
    file.write("" +  import0 + "" + os.linesep)
    file.write("" +  import1 + "" + '\n')
    file.write("" +  import2 + "" + '\n')
    file.write("" +  import3 + "" + os.linesep)

    for item in items:
        varitem = item['name']
        varip = item['ip']
        if item['type'] == 'bulb':
            file.write(f"{varitem} = Mainobject('{varip}')")
        else:
            file.write(f"{varitem} = Mainstrip('{varip}')")
        file.write("\n")
    
    file.write(os.linesep)


    for item in items:
        
        varitem = item['name']
        if item['type'] == 'bulb':
            file.write(f'#--------------------BULB---------------------{varitem}')
        else:
            file.write(f'#--------------------STRIP---------------------{varitem}')
        file.write("\n")
        for method in methods:
            file.write(f'@app.route("/{varitem}/{method}")')
            file.write("\n")
            file.write(f'def {varitem}{method}():')
            file.write("\n")
            file.write(f'   {varitem}.{method}()')
            file.write("\n")
            file.write(f'   return "<h1> Corriste escena {method} en {varitem} </h1>"')
            file.write(os.linesep)

    file.write(os.linesep)
    file.write(os.linesep)
    file.close()
