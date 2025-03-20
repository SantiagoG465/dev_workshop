import math

class Geometria:
    
    def area_rectangulo(self, base: float, altura: float) -> float:
        return base * altura

    def perimetro_rectangulo(self, base: float, altura: float) -> float:
        return 2 * (base + altura)

    def area_circulo(self, radio: float) -> float:
        return math.pi * radio**2
    
    def perimetro_circulo(self, radio):
     return 2 * math.pi * radio
    
    def area_triangulo(self, base, altura):
      return (base * altura) / 2
    
    def perimetro_triangulo_equilatero(self, lado: float) -> float:
        return 3 * lado
    
    def es_triangulo_valido(self, lado1: float, lado2: float, lado3: float) -> bool:
        return (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

    def area_trapecio(self, base_mayor: float, base_menor: float, altura: float) -> float:
        return ((base_mayor + base_menor) * altura) / 2
    
    def area_rombo(self, diagonal_mayor: float, diagonal_menor: float) -> float:
        return (diagonal_mayor * diagonal_menor) / 2
    
    def area_pentagono_regular(self, lado: float, apotema: float) -> float:
        perimetro = 5 * lado
        return (perimetro * apotema) / 2
    
    def perimetro_pentagono_regular(self, lado: float) -> float:
        return 5 * lado

    def area_hexagono_regular(self, lado: float, apotema: float) -> float:
        perimetro = 6 * lado
        return (perimetro * apotema) / 2
    
    def perimetro_hexagono_regular(self, lado: float) -> float:
        return 6 * lado

    def volumen_cubo(self, lado: float) -> float:
        return lado ** 3
    
    def area_superficie_cubo(self, lado):
        """
        Calcula el área de la superficie de un cubo.
        
        Args:
            lado (float): Longitud del lado del cubo
            
        Returns:
            float: Área de la superficie del cubo
        """
        pass
    
def volumen_esfera(self, radio):
        """
        Calcula el volumen de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Volumen de la esfera
        """
        pass
    
def area_superficie_esfera(self, radio):
        """
        Calcula el área de la superficie de una esfera.
        
        Args:
            radio (float): Radio de la esfera
            
        Returns:
            float: Área de la superficie de la esfera
        """
        pass
    
def volumen_cilindro(self, radio, altura):
        """
        Calcula el volumen de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Volumen del cilindro
        """
        pass
    
def area_superficie_cilindro(self, radio, altura):
        """
        Calcula el área de la superficie de un cilindro.
        
        Args:
            radio (float): Radio de la base del cilindro
            altura (float): Altura del cilindro
            
        Returns:
            float: Área de la superficie del cilindro
        """
        pass
    
def distancia_entre_puntos(self, x1, y1, x2, y2):
        """
        Calcula la distancia euclidiana entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Distancia entre los dos puntos
        """
        pass
    
def punto_medio(self, x1, y1, x2, y2):
        """
        Calcula el punto medio entre dos puntos en un plano 2D.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coordenadas (x, y) del punto medio
        """
        pass
    
def pendiente_recta(self, x1, y1, x2, y2):
        """
        Calcula la pendiente de una recta que pasa por dos puntos.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            float: Pendiente de la recta
        """
        pass
    
def ecuacion_recta(self, x1, y1, x2, y2):
        """
        Obtiene los coeficientes de la ecuación de una recta en la forma Ax + By + C = 0.
        
        Args:
            x1 (float): Coordenada x del primer punto
            y1 (float): Coordenada y del primer punto
            x2 (float): Coordenada x del segundo punto
            y2 (float): Coordenada y del segundo punto
            
        Returns:
            tuple: Coeficientes (A, B, C) de la ecuación de la recta
        """
        pass
    
def area_poligono_regular(self, num_lados, lado, apotema):
        """
        Calcula el área de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            apotema (float): Longitud de la apotema
            
        Returns:
            float: Área del polígono regular
        """
        pass
    
def perimetro_poligono_regular(self, num_lados, lado):
        """
        Calcula el perímetro de un polígono regular.
        
        Args:
            num_lados (int): Número de lados del polígono
            lado (float): Longitud de cada lado
            
        Returns:
            float: Perímetro del polígono regular
        """
        pass
