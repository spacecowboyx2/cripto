chave = 3
mensagem = 'Pedro estava comendo quando percebeu a cagada que fez'

#numero da letra
nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')


cifrada = ""
for caractere in mensagem:
    #find the letter in the alphabet that is in the key positions ahead
    ind = ord(caractere)
    #If it is in the secret letter range 
    if nA <= ind <= nZ:
        new_letter = chr((ind+chave)%(nZ+1) + ((ind+chave)//(nZ+1))*nA)
        cifrada = cifrada + new_letter
    elif ind in range(na, nz + 1):  
        new_letter = chr((ind+chave)%(nz+1) + ((ind+chave)//(nz+1))*na)
        cifrada = cifrada + new_letter
    else:
        cifrada = cifrada+caractere
        

print("Original: ", mensagem)
print("Cifrada: ", cifrada)