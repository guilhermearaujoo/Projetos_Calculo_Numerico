dic = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

class Numero():
    #constructor
    def __init__(self, n, b):
        
        assert(type(n)==str), "O numero deve ser passado em formato de string"
        assert(2<= b and b <= 32), f"Não é possivel criar um numero na base {b}"
        assert(type(b)==int), f"A base deve ser um número inteiro."
        if '.' in n:
            assert(0==0), "Apenas numeros inteiros são aceitos"

        self.numero = n
        self.base_original = b

    def to_decimal(self):

        # se o numero estiver na base 10, nao precisa converter
        if self.base_original==10:
            return self.numero

        # faz uma copia do numero original
        num = self.numero
        
        #faz a conversao do numero original
        dec = 0
        dec_temp = list(num)
        dec_temp.reverse()

        #se for um numero flutuante
        #if '.' in dec_temp:
            # procuro a posicao que o numero esta
        #    pos_ = dec_temp.index('.')
        #    cont = 0
            #faco uma copia do numero original
        #    dec_temp_temp = dec_temp.copy()    
            #laço do primeiro numero apos a virgula ate o ultimo
        #    for i in range(pos_ - 1, -1, -1):
                
        #        cont -= 1
        #        dec += dic.index(dec_temp_temp[i]) * self.base_original**(cont)
                #removo o numero apos a virgula
        #        dec_temp.pop(i)
        #    dec_temp.pop(0)

        for x,i in enumerate(dec_temp):
            dec += dic.index(i) * self.base_original**(x)

        #retorna um Numero do numero original convertido para base 10
        
        return Numero(str(dec), 10)


    def to_any(self, base_final):

        # se a base original for igual a base final, retorna o numero original
        if(base_final == self.base_original):
            return self

        assert(type(base_final)==int), "Operação inválida, a base final deve ser do tipo inteiro."
        assert(2<= base_final and base_final <= 32), f"Não é possivel criar um numero na base {base_final}"

        # transforma o numero orignial em decimal
        num = Numero(self.to_decimal(), 10)
        num_dec = int(num.numero)

        # transforma o numero decimal para a base final
        numero_final_temp = []
        numero_final = ''
        while True:
            
            temp_numero_final = num_dec%base_final
            numero_final_temp.append(temp_numero_final)

            if int(num_dec/base_final) == 0:
                break
            num_dec = int(num_dec/base_final)

        # faz um copia do numero na final final para a posicao correta
        numero_final_temp.reverse()
        for i in numero_final_temp:
            numero_final += dic[i]  

        # retorna um classe Numero do numero original para a base final
        
        return Numero(numero_final, base_final)


    def next(self):
        # transforma o numero em decimal
        num_ = self.to_decimal()
        # soma 1 ao numero
        num_.numero = str(int(num_.numero) + 1)
        # transforma o numero na base original
        num_final = num_.to_any(self.base_original)

        # retorna o numero sucessor na base original
        return num_final


    def prior(self):
        # transforma o numero em decimal
        num_ = self.to_decimal()
        # soma 1 ao numero
        num_.numero = str(int(num_.numero) - 1)
        # transforma o numero na base original
        num_final = num_.to_any(self.base_original)

        # retorna o numero sucessor na base original
        return num_final


    def __add__(self, another):
        #pode somar Numero + Numero e Numero + string
        
        # verifica se another é uma classe Numero, se não for criar uma classe com o another e a original de self
        if isinstance(another, Numero):
            other = another
        else:
            assert(type(another)==str), f"Impossivel somar {type(self)} com {type(another)}"
            other = Numero(another, self.base_original)


        assert(self.base_original == other.base_original), "Os números precisam ter a mesma base"

        # soma duas classes
        num_temp = int(self.to_decimal()) + int(other.to_decimal())
        
        soma_temp = Numero(str(num_temp), 10)
        soma_final = soma_temp.to_any(self.base_original)

        #retorna a soma na base de self
        return soma_final


    def __radd__(self, other):
      #caso em que "string" + Numero
      return self.__add__(other)

    def __mul__(self, another):
        #pode multiplicar Numero + Numero e Numero + string
        
        # verifica se another é uma classe Numero, se não for criar uma classe com o another e a original de self
        if isinstance(another, Numero):
            other = another
        else:
            assert(type(another)==str), f"Impossivel multiplicar {type(self)} com {type(another)}"
            other = Numero(another, self.base_original)


        assert(self.base_original == other.base_original), "Os números precisam ter a mesma base"

        # multiplica duas classes
        num_temp = int(self.to_decimal().numero) * int(other.to_decimal().numero)
        
        mult_temp = Numero(str(num_temp), 10)
        mult_final = mult_temp.to_any(self.base_original)

        #retorna a soma na base de self
        return mult_final

    def __rmul__(self, other):
      #caso em que "string" * Numero
      return self.__mul__(other)

    def __str__(self):
        return f"numero: {self.numero} base: {self.base_original}"


n1 = Numero('10', 10)
n2 = Numero('1', 10)

n3 = n1+n2
 
print(n3.to_any(16))
