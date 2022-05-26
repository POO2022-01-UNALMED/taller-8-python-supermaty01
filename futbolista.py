from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, años, goles, tarjetas, pierna):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", años)
        self._golesMarcados = goles
        self._tarjetasRojas = tarjetas
        self._piernaHabil = pierna
        Futbolista.listaFutbolistas.append(self)


    def  getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, _golesMarcados):
        self._golesMarcados = _golesMarcados

    def  getTarjetasRojas(self):
        return self._tarjetasRojas

    def set_tarjetasRojas(self, _tarjetasRojas):
        self._tarjetasRojas = _tarjetasRojas

    def  getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, _piernaHabil):
        self._piernaHabil = _piernaHabil


    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self._nombre, self._deporte, self._edad, self._añosPracticando)