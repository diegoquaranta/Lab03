from operator import attrgetter

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.codice} , {self.tipo}, {self.marca}, {self.anno_acquisto}, {self.valore} euro"





class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.codice = codice
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__ (self):
        return f"{self.codice}, {self.data}, {self.id_strumento}, {self.cognome_allievo}"





class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = {}
        self.prestiti = {}
        self.ultimo_id_prestito = 0  #ricorda messo qui mi permette di poter sggiornare subito l'id prestito

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        with open(file_path, "r", encoding="utf8") as f:
            righe = f.readlines()

            for i in range(len(righe)):
                righe[i] =righe[i].strip().split(",")

            for riga in righe:
                codice = riga[0]
                tipo = riga[1]
                marca = riga[2]
                anno_acquisto = riga[3]
                prezzo = riga[4]
                strumento = Strumento(codice, tipo, marca, int(anno_acquisto), float(prezzo))
                self.strumenti[codice]= strumento


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        numero = 0

        for codice in self.strumenti.keys():
            numero_codice = int(codice[1:])

            if numero_codice > numero:
                numero = numero_codice

        numero = numero + 1
        nuovo_codice = "S" + str(numero)

        strumento = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.strumenti[nuovo_codice] = strumento

        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        stru = list(self.strumenti.values())
        strumenti_ordinati= sorted(stru, key=attrgetter("marca"))
        return strumenti_ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception ("Strumento non presente nel deposito")

        for prestito in self.prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception ("Strumento già in prestito")

        self.ultimo_id_prestito += 1
        codice =  "P" + str(self.ultimo_id_prestito)

        prestito = Prestito(codice, data, id_strumento, cognome_allievo)

        self.prestiti[codice] = prestito

        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception ("Prestito non presente")

        del self.prestiti[id_prestito]
