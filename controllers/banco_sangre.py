import models.clases as c

class Registro:
    def __init__(self):
        self.donantes_activos = c.Pila()
        self.donantes_revertidos = c.Pila()

    def registrar_donante(self, nombre_donante):
        if not nombre_donante or not isinstance(nombre_donante, str):
            raise ValueError("Porfavor esrcriba el nombre del donante.")

        if self.donantes_activos.ver_tope():
            self.donantes_revertidos = c.Pila()

        self.donantes_activos.push(nombre_donante)
        return f"Se ha registrado a {nombre_donante} con exito!"

    def atender_ultimo_donante(self):
        if self.donantes_activos.esta_vacia():
            return "No hay donantes para atender."

        donante_atendido = self.donantes_activos.pop()
        self.donantes_revertidos.push(donante_atendido)
        return f"Donante atendido: {donante_atendido}"

    def rehacer_atencion(self):
        if self.donantes_revertidos.esta_vacia():
            return "No hay atenciones para rehacer."

        donante_revertido = self.donantes_revertidos.pop()
        self.donantes_activos.push(donante_revertido)
        return f"Se ha revertido la atencion de {donante_revertido}"

    def obtener_donantes(self):
        if self.donantes_activos.esta_vacia():
            return "No hay donantes en espera."
        
        return f"Donantes en espera: {', '.join(self.donantes_activos.donantes)}"