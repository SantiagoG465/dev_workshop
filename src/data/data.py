class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):

        lista_invertida = []
        for i in range(len(lista) -1, 1, -1):
            lista_invertida.append(lista[i])

        return lista_invertida
        
    
    def buscar_elemento(self, lista, elemento):

        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
       
        return -1

        pass
    
    def eliminar_duplicados(self, lista):

        lista_sin_duplicados = []
        for elementos in lista:
            if elementos not in lista_sin_duplicados:
                lista_sin_duplicados.append(elementos)


        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1: list, lista2: list) -> list:
        i, j = 0, 0
        resultado = []
        
        while i < len(lista1) and j < len(lista2):
            if lista1[i] < lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        
        return resultado
    
    def rotar_lista(self, lista, k):
        
        k = k % len(lista) 
        
        return lista[-k:] + lista[:-k]
    
    pass
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
       
        suma_total = n * (n + 1) // 2
        suma_lista = sum(lista)
        return suma_total - suma_lista
        
    
    def es_subconjunto(self, conjunto1, conjunto2):
     
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False
        return True
        
    
    def implementar_pila(self):
            def __init__(self):
              self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # O lanzar una excepción

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


    def implementar_cola(self):
            def __init__(self):
                self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None  # O lanzar una excepción

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0
        
    
    class Matriz:
        def matriz_transpuesta(self, matriz: list) -> list:
            return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

    