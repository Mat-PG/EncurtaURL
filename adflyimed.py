import base64
import pickle
import os
from math import floor

class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = "urls.dat"
        self.indice = 1000 + len(self.dic)

    def loadDic(self):
        self.__load_dic()

    def __load_dic(self):
        if os.path.isfile(self.nome_arq):
            arq = open(self.nome_arq,"rb")
            self.dic = pickle.load(arq)
            arq.close()
            self.indice = 1000 + len(self.dic)

    def saveDic(self):
        self.__save_dic()

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
        curto = e.toBase(self.indice)
        if "www." in url:
            i = 12
            url_curta = ""
            while url[i] != ".":
                url_curta += url[i]
                i += 1
            url_curta += ".to/"+curto
        else:
            i = 8
            url_curta = ""
            while url[i] != ".":
                url_curta += url[i]
                i += 1
            url_curta += ".to/"+curto
        print("url ecurtada: "+url_curta)
        tupla = (url_curta,url)
        self.dic[self.indice] = tupla
        self.toBase(self.indice)
        self.indice = self.indice + 1

    def buscar(self, url_curta):
        indice = self.to10(url_curta)
        return self.dic[indice][1] # retorna a 2a posicao da tupla

    def listar_urls(self):
        print(self.dic)

## TESTES ##
e = Encurtador()
while True:
    print("")
    print("--------------------------------------------------------------")
    print("Escolha uma das opções: ")
    print("Fechar programa [0]")
    print("Carregar arquivo [1]")
    print("Salvar tabela [2]")
    print("Encurtar url [3]")
    print("Mostrar tabela [4]")
    try:
        resposta = int(input())
        os.system('cls')
        if resposta == 0:
            break
        if resposta == 1:
            e.loadDic()
            print("-----Carregado-----")
            os.system('cls')
        if resposta == 2: 
            e.saveDic()
            print("------Salvo-----")
        if resposta == 3:
            print("")
            url = str(input("Qual url deseja encurtar? "))
            e.encurtar(url)
            os.system('cls')
        if resposta == 4: 
            print("")
            e.listar_urls()
    except(ValueError):
        os.system('cls')
        print("Insira uma resposta válida!!!")
    except(IndexError):
        print("Insira uma url válida!!!")
    except(EOFError):
        print("Arquivo Vazio!!!")


#https://www.vivaolinux.com.br/dica/Python-3.0-Gravando-dicionarios-em-arquivos/
#https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/
