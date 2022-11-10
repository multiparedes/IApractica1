"""
ClauPercepcio:
    POSICIO = 0
    OLOR = 1
    PARETS = 2
"""

import copy
from itertools import product
from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import ClauPercepcio, AccionsRana, Direccio


class Rana(joc.Rana):
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)

    def pinta(self, display):
        pass

    def actua(
            self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        Estat.generar_fills()
        return AccionsRana.ESPERAR

class Estat:
    def __init__(self, pare = None):
        self.__pare = pare

    def __eq__(self, other):
        if self[ClauPercepcio.POSICIO] == other[ClauPercepcio.POSICIO]:
            return True
        else:
            return False 

    #La granota esta damunt la pizza.
    def es_meta(self) -> bool:
        if self[ClauPercepcio.POSICIO] == self[ClauPercepcio.OLOR]:
            return True
        else:
            return False 

    #La posició pasada per paràmetre no és una paret i està dins el tauler.
    def es_possible(self) -> bool:
        #Checkeam cordenada X, Y i si no es troba damunt una paret.
        if self[ClauPercepcio.POSICIO][0] < 0 and self[ClauPercepcio.POSICIO][0] > 8:
            if self[ClauPercepcio.POSICIO][1] < 0 and self[ClauPercepcio.POSICIO][1] > 8:
                if self[ClauPercepcio.POSICIO] not in self[ClauPercepcio.PARETS]:
                    return True
        return False            

    #Genera tots els possibles filles a partir del nostre estat actual.
    def generar_fills(self) -> list:
        l_accions = [AccionsRana.MOURE, AccionsRana.BOTAR]
        l_direccions = [Direccio.BAIX, Direccio.DALT, Direccio.DRETA, Direccio.ESQUERRE]

        for accio in product(l_accions, l_direccions):
            print(accio)

    @property
    def pare(self):
        return self.__pare

    @pare.setter
    def pare(self, value):
        self.__pare = value