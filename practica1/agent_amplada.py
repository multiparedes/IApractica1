from ia_2022 import entorn
from practica1 import joc
from practica1.entorn import AccionsRana, ClauPercepcio, Direccio
from practica1.agent import Rana, Estat


class Rana(joc.Rana):
    def __init__(self, *args, **kwargs):
        super(Rana, self).__init__(*args, **kwargs)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None


    def pinta(self, display):
        pass

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(info=percep.to_dict(), pes = 0, meta = percep[ClauPercepcio.OLOR], cord=percep[ClauPercepcio.POSICIO][self.nom])

        if self.__accions == None:
           self._cerca(estat=estat, percep = percep)
        
        while len(self.__accions) >= 0:
            return self.__accions.pop()

    def _cerca(self, estat: Estat, percep: entorn.Percepcio):
        self.__oberts = []
        self.__tancats = set()

        self.__oberts.append(estat)
        actual = None
        while len(self.__oberts) > 0:
            #eliminam l'estat actual de oberts
            actual = self.__oberts[0]
            self.__oberts = self.__oberts[1:]

            #per evitar bucles
            if actual in self.__tancats:
                continue
            
            #miram si és meta
            if actual.es_meta():
                #sortim del while
                break

            #no era l'estat meta si hem arribat aqui
            estats_fills = actual.generar_fills()

            #afegim els es fills a oberts --> el while seguirà fins que arribem al meta i no es generin més fills
            for eFill in estats_fills:
                self.__oberts.append(eFill)
            
        #hem sortit del while
        #anam guardant l'accio i miram el pare
        if actual.es_meta():
            accions = []
            iterador = actual
            #perquè quan arribi s'hi quedi un torn extra
            #ho posam primer perquè serà lo darrer q treurà
            accions.append(AccionsRana.ESPERAR)

            while iterador.pare is not None:
                pare, accio = iterador.pare

                accions.append(accio)
                #Si afegim botar, afegim esperar automàticament perquè perdem torn
                if(accio == AccionsRana.BOTAR):
                    accions.append(AccionsRana.ESPERAR)
                iterador = pare
            self.__accions = accions
            return True