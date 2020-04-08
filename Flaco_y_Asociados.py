
# LUIS JOSE RODRIGUEZ  CI: 27.100.925
"""---------------------------------------------CLASE Archivo---------------------------------------"""
"""NOTA: profe esta clase tiene sus metodos completos, para trabajar con archivos pero no los añadi """
"""porque tienen un error de index out of range. al leer el archivo linea a linea siempre me quedaba una linea blanca al final"""
""" no pude solucionar ese error a tiempo, disculpe"""
class Archivo:
    def __init__(self):
        self.nombre="articulos.txt"

    def linea_to_articulo(self,linea):
        lista= linea.split("%") 
        print("codigo prueba"+lista[0])
        art= Articulo(lista[0],lista[1],lista[2],lista[3],lista[4],lista[5])   
        return(art)

    def articulo_to_linea(self,art):
        linea= art.codigo+ "%" + art.nombre +"%" +art.descripcion +"%" +art.categoria +"%"+str(art.precio)+"%"+str(art.disponibles)
        return linea            

    def archivar_lista(self,lista):
        texto=""
        f= open (self.nombre,'w') 
        primero=True       
        for articulo in lista:
            if primero:
                texto= self.articulo_to_linea(articulo)
                primero=False
            else:
                texto= "\n" + self.articulo_to_linea(articulo)     
        f.write(texto)
        f.close()

    def cargar_archivo(self,la):
        f= open (self.nombre,'r')            
        for linea  in f:
            print("entre")
            art= self.linea_to_articulo(linea)
            la.agregar_articulo(art)
        



"""---------------------------------------------CLASE Caja---------------------------------------"""
""" Es un objeto sencillo que Contiene datos relacionados al dinero """
class Caja:
    def __init__(self):
        self.vdolar=100000
        self.generado = 0.0

    def aumentar_generado(self, cant):
        self.generado = self.generado + cant 

    def modificar_dolar(self, dolar):
        self.vdolar= dolar   

"""---------------------------------------------CLASE Articulo---------------------------------------"""

class Articulo:
    def __init__(self,codigo,nombre,descripcion,categoria,precio,cant_disponible):
        self.codigo=codigo
        self.nombre=nombre
        self.descripcion = descripcion
        self.categoria=categoria
        self.precio=precio
        self.disponibles=cant_disponible      
    
    #def agregar(self, cantidad):
    #    self.disponibles =  self.disponibles + cantidad


    def vender(self, cantidad):
        self.disponibles = self.disponibles - int(cantidad)

    def mostrar(self,i,caja):
        print(str(i)+".[CODIGO:"+self.codigo+"] producto: "+self.nombre+":")
        print("     categoria: "+self.categoria)
        print("     precio bs: "+str(self.precio*caja.vdolar)+" bs")  
        print("     precio USD: "+ str(self.precio)+" $")
        print("     disponibles: "+str(self.disponibles))

    def modificar_cantidad(self, cantidad):
        self.disponibles=cantidad    
"""---------------------------------------------CLASE ListaArticulos---------------------------------------"""
""" utilizada para almacenar y manippular los diferentes articulos (es probablemente la clase mas usada en el proyecto)"""
""" tambien es la que tiene mas metodos                                                                                 """

class listaArticulos:
    def __init__(self):
        self.la = []
        self.numero_articulos=0

    def existe_articulo(self, codigo):
        i=0
        existe = False
        for articulo in self.la:            
            if articulo.codigo == codigo:
                existe=True
            i=i+1
        return existe
  
    def agregar_articulo(self,  Articulo):
        self.la.append(Articulo)
        self.numero_articulos=self.numero_articulos+1

    def obtener_articulo(self, codigo):
        i=0
        encontrado= False
        while (not encontrado) and (i<self.numero_articulos):
            if self.la[i].codigo == codigo:
                encontrado=True
                aux=self.la[i]
        return aux 

    def get_pos(self,codigo):
        i=0
        encontrado= False
        while (not encontrado) and (i<self.numero_articulos):
            if self.la[i].codigo == codigo:
                encontrado=True
            i=i+1
        return i-1     

    def eliminar_articulo (self, codigo):
        self.la.remove(  self.obtener_articulo(codigo)  )
        self.numero_articulos = self.numero_articulos -1

    def mostrar_articulos(self,caja):
        i=1
        for articulo in self.la:            
            articulo.mostrar(i,caja)
            i=i+1
    
    def mostrar_agotados (self):
        i=1 
        for articulo in self.la:
            if articulo.disponibles==0:
                print(str(i)+".["+articulo.codigo+"]"+articulo.nombre)    

    def modificar_cantidad (self,codigo,cantidad):
        self.la[self.get_pos(codigo)].modificar_cantidad(cantidad)  

    def obtener_el_mas_costoso(self,caja):
        primero=True
        articulo=""
        for articulo in self.la:
            if primero: 
                mas_costoso= articulo
                primero=False
            else:    
                if articulo.precio > mas_costoso.precio:
                    mas_costoso = articulo;     
        print ("[CODIGO: "+mas_costoso.codigo+"] Nombre: "+mas_costoso.nombre + " USD:"+ str(mas_costoso.precio)+"$"+" Precio Bs:"+ str(mas_costoso.precio*caja.vdolar))
    
    def obtener_el_mas_econmico(self,caja):
        primero=True
        articulo=""
        for articulo in self.la:
            if primero: 
                mas_econmico= articulo
                primero=False
            else:    
                if articulo.precio < mas_econmico.precio:
                    mas_econmico = articulo;    
        print ("[CODIGO: "+mas_econmico.codigo+"] Nombre: "+mas_econmico.nombre + " USD:"+ str(mas_econmico.precio)+"$"+" Precio Bs:"+ str(mas_econmico.precio*caja.vdolar))    

    def vender(self, codigo, cantidad, caja):
        if (self.la[self.get_pos(codigo)].disponibles >= int(cantidad)):
            self.la[self.get_pos(codigo)].vender(cantidad)

            caja.aumentar_generado(self.la[self.get_pos(codigo)].precio * float (cantidad)) 
            #generado = float (self.la[self.get_pos(codigo)].precio) * float (cantidad)
        else:
            print(" Error: no tenemos la cantidad deseada de ese producto")    

"""---------------------------------------------Metodos para solicitar datos---------------------------------------""" 
""" para ahorrar lineas de codigo, hice funciones que permiten solicitar un TD en especifico pasando una etiqueta """           

#etiqueta es una variable string que se utiliza para dar un encabezado a la pregunta 
def pedirNumeroEntero(solicitud):  #confirma que el numero ingresado sea valido (como un entero)

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(solicitud))
            correcto=True
        except ValueError:
            print('Error: debe ingresar un numero entero')
    return num

def pedirNumeroReal(solicitud):  #confirma que el numero ingresado sea valido (como un entero)
    correcto= False
    String ="" #variable que almacena el valor devuelto por la funcion que solicita
    while not correcto:
        try:
            String = float(input(solicitud))
            correcto = True
        except ValueError:
            print('Error:')  
    return String   

def pedirString(solicitud): #dolicitud es el encabezado de la pregunta
    correcto= False
    String ="" #variable que almacena el valor devuelto por la funcion que solicita
    while not correcto:
        try:
            String = str(input(solicitud))
            #correcto =True
            if (not String == ""):
                correcto = True
        except ValueError:
            print('Error:')  
    return String           



"""---------------------------------------------SubMenus---------------------------------------"""
"""                               menus desprendidos del menu principal                        """

def menuCaja(la, caja): #menu del cajero      #este menu es la vista que tendra el cajero o cajera durante su jornada de trabajo
    #otro =  otro cliente llego a la caja
    #mas = mas productos para ese cliente
    otro="s"
    mas="s"
    
    while (otro == "s"): 
        mas =="s"
        while(mas== "s"):
            codigo = pedirString("Codigo del producto: ")
            if la.existe_articulo(codigo):
                cantidad = pedirString("cantidad: ")
                la.vender(codigo,cantidad,caja)
            else: 
                print("El codigo ingresado no pertenece a ningun producto")    
            mas = pedirString("¿otro producto?(s/n): ")  
        otro = pedirString("¿otro cliete? (s/n): ")


def menuAdmin(la,caja): #menu de administracion (solo puede ingresar el usuario administrador)
    salir = False
    opcion = 0 
    contraseña = pedirString("contraseña Administrador //es admin profe: ")
    if (contraseña != "admin"):
        print("ERROR: contraseña equivocada")
    else:    
        while not salir:
            print ("\n"+"::MENU DE USUARIO ADMINISTRADOR")
            print ("1. Registrar un nuevo articulo")
            print ("2. Mostrar articulos")
            print ("3. Eliminar articulo del inventario")
            print ("4. modificar cantidad de un articulo en inventario")
            print ("5. modificar el valor actual del dolar")
            print ("6. Salir")   
 
            opcion = pedirNumeroEntero("Ingrese una opcion: ")

            if opcion == 1: # Registrar un nuevo articulo 
                codigo= pedirString("Ingrese el codigo del producto: ") 
                if (la.existe_articulo(codigo)):
                    print("ERROR: el codigo '"+codigo+"' se encuentra registrado")
                else:          
                    nombre= pedirString("Ingrese el nombre del producto: ")
                    descripcion= pedirString("Ingrese la descripcion del producto: ")
                    categoria= pedirString("Ingrese la categoria del producto: ")
                    precio= pedirNumeroReal("Ingrese el precio del producto (en dolares): ") 
                    cant_disponible= pedirNumeroEntero("Ingresee la cantidad en inventario: ")
                    nuevo= Articulo(codigo,nombre,descripcion,categoria,precio,cant_disponible)
                    la.agregar_articulo(nuevo)
                    print("MENSAJE: articulo agregado con exito")

            elif opcion == 2: #lista de articulos
                if la.numero_articulos>0:
                    print("::LISTA DE ARTICULOS:")
                    la.mostrar_articulos(caja)
                else:
                    print("MENSAJE: actualmente no hay productos")  

            elif opcion ==3: #eliminar articulos del inventario
                print( "Eliminando..." )
                codigo= pedirString("Ingrese el codigo del producto que desea eliminar: ") 
                if (not la.existe_articulo(codigo)):
                    print("ERROR: el codigo '"+codigo+"' no pertenece a ningun producto registrado")
                else:
                    la.eliminar_articulo(codigo)
                    print("eliminado exitosamente")

            elif opcion ==4: #modificar cantidad de articulos en el inventario
                codigo = pedirString("Ingrese el codigo del articulo del cual desea editar su cantidad: ")
                if (not la.existe_articulo(codigo)):
                    print("ERROR: el codigo '"+codigo+"' no pertenece a ningun producto registrado")
                else:
                    correcto= False
                    while not correcto: 
                        cant = pedirNumeroEntero("Ingrese la nueva cantidad de productos del mismo tipo("+codigo+"): ")
                        if (cant >=0):
                            correcto =True 
                            la.modificar_cantidad(codigo,cant)  
            elif opcion == 5:  
                dolar = pedirNumeroReal("ingrese el valor actual del dolar(USD) en bolivares(Bs): *ejmp: 450000*" + "\n") 
                caja.modificar_dolar(dolar)
                print("Modificado con exito el nuevo valor actual del dolar es : "+ str(caja.vdolar))
            elif opcion == 6:
                salir = True
            else:
                print ("la opcion ingresada no es valida, ingrese un numero entre 1 y 3")

if __name__ == "__main__":    #EL MAIN CONTIENE EL MENU PRINCIPAL
    la = listaArticulos()
    caja = Caja()
    salir = False
    opcion = 0    
    #txt= Archivo() se supone que aqui se hace la instancia del archivo pero como acote anteriormente el archivo tiene fallas disclupe profe 
    
    while not salir: #opciones del menu principal
        print ("\n"+":: CONTROL DE MERCANCIA FLACO Y ASOCIADOS")
        print ("1. Caja")
        print ("2. Admin")
        print ("3. Info ")
        print ("4. Salir")   
                
        opcion = pedirNumeroEntero("Ingrese una opcion: ")
 
        if opcion == 1:  # envia a la pantalla desde donde trabaja la cajera o cajero
            menuCaja(la,caja) #LA : lista de articulos, caja: es un objeto que contiene datos relacionados con el dinero

        elif opcion == 2: # envia al menu admin 
            menuAdmin(la,caja)

        elif opcion ==3: # despliega informacion de "FlAco y asociados"
            print(":: INFORMACION:")
            print("*DOLAR HOY: ")
            print("  1 dolar = "+ str(caja.vdolar))
            print("*Generado (equivalente en dolares):")
            print("  "+str(caja.generado)+"$") 
            print("*Generado (equivalente en bolivares):")
            print("  "+str(caja.generado*caja.vdolar)+"bs") 
            if (la.numero_articulos>0):
                print("*PRODUCTO MAS COSTOSO: ")
                la.obtener_el_mas_costoso(caja)
                print("*PRODUCTO MAS ECONOMICO: ")
                la.obtener_el_mas_econmico(caja)
                print("*ARTICULOS AGOTADOS:")
                la.mostrar_agotados()

        elif opcion == 4: 
            salir = True
        else:
            print ("la opcion ingresada no es valida, ingrese un numero entre 1 y 4")
    pass

