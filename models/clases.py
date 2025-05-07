class Pila:
    def __init__(self):
        self.donantes = []
    
    def push(self, donante):
        self.donantes.append(donante)
    
    def pop(self):
        if not self.esta_vacia():
            return self.donantes.pop()
        return None
    
    def ver_tope(self):  # Cambiado de peek a ver_tope
        if not self.esta_vacia():
            return self.donantes[-1]
        return None
    
    def esta_vacia(self):
        return len(self.donantes) == 0