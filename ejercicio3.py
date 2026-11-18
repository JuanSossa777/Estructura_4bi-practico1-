class nodo:
    def __init__(self, dato):
        self.dato = dato #guardamos el dato del nodo
        self.siguiente = None  #apuntador siguiente
        self.anteriorn = None  #apuntador anterior

class ListaDoble:
    
    def __init__(self):
        self.inicio= None  #inicializamos la cabeza de la lista
        self.fin = None  #inicializamos el final de la lista

    def insertar_al_inicio (self, dato):
        nuevo = nodo(dato)  #creamos un nuevo nodo en la lista
        if self.inicio is None:  #si el nodo esta vacio?
            self.inicio = nuevo  #opcion true (el inicio toma el valr del nuevo nodo)
            self.fin = nuevo  # (como el final toma el valor del nuevo nodo)
        else:
            nuevo.siguiente = self.inicio #el nuevo agarra al que era primero
            self.inicio.anterior = nuevo  #el viejo primero agarra al nuevo
            self.inicio = nuevo  #actualizamos datos

    def insertar_al_final (self, dato):
        nuevo = nodo(dato) 
        if self.fin is None:  
            self.inicio = nuevo  
            self.fin = nuevo  
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin 
            self.fin = nuevo  

    def imprimir(self):
        actual = self.inicio  #inicializamos el nodo actual
        while actual is not None:  #mientras el nodo actual no sea nulo
            print(actual.dato)  #imprimimos el dato del nodo actual
            actual = actual.siguiente  #actualizamos el nodo actual al siguiente
        print("Fin de la lista")  #mensaje de fin de la lista

tren_nodo = ListaDoble()

tren_nodo.insertar_al_final(10)
tren_nodo.insertar_al_final(20)
tren_nodo.insertar_al_inicio(30)
tren_nodo.imprimir()  # Llamada al método imprimir para mostrar la lista
