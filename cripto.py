#mensagem para cifrar
#chave para criptografar
#cifra de cezar

alfabeto = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chave = 3
mensagem = "abacaxi"
#n = len(alfabeto) #tamanho do alfabeto
#tabela ascii
n = 128
cifrada = ""
for letter in mensagem:

    #achar no alfabeto a letra que esteja chave e posição a frente
    #indice = alfabeto.index(letter)
    #nova_letra = alfabeto[(chave+indice)%n]
    indice = ord(letter) #usando função do python- ord retorna o número do caractere
    nova_letra = chr((indice+chave)%n) #chr retorna o caractere 
    #substituir na mensagem a letra pela nova letra
    cifrada = cifrada + nova_letra

print(mensagem)
print(cifrada)
