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
from practica1.entorn import AccionsRana, ClauPercepcio, Direccio


class Rana(joc.Rana):
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)

    def pinta(self, display):
        pass

    def actua(
            self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        pass

class Estat:
    def __init__(self, info: dict, pes = None, pare = None, meta = None, cord = None):  
        self.__info = info
        self.__pes = pes
        self.__pare = pare
        self.__meta = meta
        self.__cord = cord
        

    UTILITATS = {
        Direccio.BAIX: (0, 1),
        Direccio.DRETA: (1, 0),
        Direccio.DALT: (0, -1),
        Direccio.ESQUERRE: (-1, 0),
        AccionsRana.BOTAR: 6,
        AccionsRana.MOURE: 1
    }

    def __hash__(self):
        return hash(self.__pare)

    def __getitem__(self, key):
        return self.__info[key]

    def __setitem__(self, key, value):
        self.__info[key] = value

    def __eq__(self, other):
        return self.__cord == other[ClauPercepcio.POSICIO]

    #La granota esta damunt la pizza.
    def es_meta(self) -> bool:
        return self.__meta == self.__cord

    #La posició pasada per paràmetre no és una paret i està dins el tauler.
    def es_possible(self) -> bool:
     #Checkeam cordenada X, Y i si no es troba damunt una paret.
        if self.__cord[0] > 0 and self.__cord[0] < 8:
            if self.__cord[1] > 0 and self.__cord < 8:
                if self.__cord not in self[ClauPercepcio.PARETS]:
                    return True
        return False            

    #Genera tots els possibles filles a partir del nostre estat actual.
    def generar_fills(self) -> list:
        l_accions = [AccionsRana.MOURE, AccionsRana.BOTAR]
        l_direccions = [Direccio.BAIX, Direccio.DALT, Direccio.DRETA, Direccio.ESQUERRE]

        fills = list()

        for accio in product(l_accions, l_direccions):
            possible_fill = copy.deepcopy(self)
            possible_fill.__pare = (self, accio)

            possible_fill.__pes =+ self.UTILITATS.get(accio[0])

            #sumar tuples, coordenades pare + moviment del fill que estam creant
            if accio == AccionsRana.BOTAR:
                possible_fill.__cord = tuple(map(sum, zip(self.UTILITATS.get(accio[1]*2), possible_fill.__cord)))
            else:
                possible_fill.__cord = tuple(map(sum, zip(self.UTILITATS.get(accio[1]), possible_fill.__cord)))

            if possible_fill.es_possible:
                fills.append(possible_fill)
            
        return fills

    #Per l'heurística emprarem la distància de Manhattan.
    def calc_heuristica(self) -> int:
        return (abs(self.__cord[0] - self[ClauPercepcio.OLOR][0]) + abs(self.__cord[1] - self[ClauPercepcio.OLOR][1]))

    @property
    def pare(self):
        return self.__pare

    @pare.setter
    def pare(self, value):
        self.__pare = value