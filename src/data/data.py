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
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        pass
    
    def eliminar_duplicados(self, lista):

        lista_sin_duplicados = []
        for elementos in lista:
            if elementos not in lista_sin_duplicados:
                lista_sin_duplicados.append(elementos)


        return lista_sin_duplicados
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada

            lista1 = [1, 3, 5, 7]
        
            lista2 (list): Segunda lista ordenada

            lista2 = [2, 4, 6, 8]

            lista1 = [1, 3, 5, 7]


        resultado = combinar_listas_ordenadas(lista1, lista2)
        print(resultado)  [1, 2, 3, 4, 5, 6, 7, 8]

        Con esta implementación,  eficientemente dos listas ordenadas en una sola lista ordenada.

            
        Returns:
            list: Lista combinada y ordenada
        """
        pass
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        pass
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        pass
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pass
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        pass
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        pass