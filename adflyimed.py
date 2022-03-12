import pickle
import os
from math import floor

class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = "urls.dat"
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        if os.path.isfile(self.nome_arq):
            arq = open(self.nome_arq,"rb")
            self.dic = pickle.load(arq)
            arq.close()

    def __save_dic(self):
        arq = open(self.nome_arq, "wb")
        pickle.dump(self.dic,arq)
        arq.close

    def toBase(self, num, b = 62):
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        r = num % b
        res = base[r];
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b = 62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        limit = len(num)
        res = 0;
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        tupla = (self.toBase(self.indice),url)
        self.dic[self.indice] = tupla
        self.indice = self.indice + 1
        self.__save_dic()
        
        # salvar no dicionario usando como chave o valor da variavel self.indice
        # o valor a ser salvo é uma tupla onde a posicao 0 eh o indice convertido
        # para string usando base62 e a posicao 1 eh a url original
        # nao esqueca de incrementar a variavel self.indice
        # e por fim, chamar o metodo __save_dic para salvar o dicionario no arquivo em disco.

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1] # retorna a 2a posicao da tupla

    def listar_urls(self):
        print(self.dic)
   
## TESTES ##
os.system('cls')
e = Encurtador()
e.encurtar("https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/")
e.listar_urls()

print(e.buscar('g8'))