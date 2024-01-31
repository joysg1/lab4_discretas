#conjunto de prueba general 
A = {1, 2, 3}
R = {(1, 2), (2, 3), (1, 3)}
R1 = {(1, 2), (2, 3), (1, 3), (3, 1)}


# Conjuntos y relaciones de prueba para reflexividad

A1 = {1,2,3,4,5}
R1 = {(1,1),(2,2),(3,3), (4,4), (5,5)}
R2 = {(1,1), (2,3), (3,3)}

# Conjuntos y relaciones de prueba para irreflexivilidad 

A2 = {"a", "b", "c"}
R3 = {("a","b"), ("c","a")}
R4 = {("a", "a"), ("b","c"), ("a","b")}


# Conjuntos y relaciones de prueba para simetria

A3 = {"u","v","w"}
R5 = {("u","v"), ("v","u"), ("w","u"), ("u","w")}
R6 = {("u","x"), ("x", "v"), ("x", "x")}

# Conjuntos y relaciones de prueba para asimetria

A4 = {1,2,3,4}
R7 = {(1,2), (3,4), (3,1)}
R8 = {(4,3), (3,4), (1,2)}


# Conjuntos y relacones de prueba para antisimetria

A5 = {1,2,3,4}
R8 = {(1,4),(4,1),(2,3),(3,2)}

A6 = {1, 2, 3}
R9 = {(1, 2), (2, 3)}


# Conjuntos y relaciones de prueba para transitividad

A7 = {1, 2, 3}
R10 = {(1, 2), (2, 3), (1, 3)}
R11 = {(1, 2), (2, 3), (1, 3), (3, 1)}


# Conjunto y relacion de prueba (simetrica y no trasitiva)

A8 = {"a","b","c","d"}
R12 = {("a","b"), ("b","a"),("c","d"),("d","c")}


# Conjunto y relacion de prueba (antisimetrica y transitiva)

A9 = {"w","x","y"}
R13 = {("w","x"), ("x","y"),("w","y")}


# Conjunto y relacion de prueba (irreflexiva y no transitiva)

A10 = {5,4,3,2,1}
R14 = {(5,2), (3,1), (4,3), (2,4)}


# Conjunto y relacion de prueba (reflexiva y no simetrica)

A11 = {"d","e","f"}
R15 = {("d","d"),("e","e"),("f","f"),("e","d"),("f","d")}


# Conjunto y relacion de prueba (simetria y antisimetria)

A12 = {1,2,3}
R16 = {(1,1), (2,2), (3,3)}


# Conjunto y relaciones de prueba (definida en todas partes)

A13 = {8,9,10,11,12}
R17 = {(8,9),(11,11),(9,9)}
R18 = {(9,12),(8,10),(10,9),(11,9),(12,10)}


# Conjunto y relaciones de prueba (uno a uno)

A14 = {3,4,5,6,7}
R18 = {(3,4),(4,5),(5,6)}
R19 = {(5,6),(6,6),(3,3),(4,3),(5,7)}


# Conjunto y relaciones de prueba (exhaustiva)

A15 = {1,4,5}
R20 = {(1,1),(4,4),(5,5)}
R21 = {(1,4), (5,1)}

print("\n");
print("PROBLEMAS # 1");

def es_reflexiva(A, R): # Definicion de la funcion 
 for e in A:           # Ciclo for para recorrerer los elementos
     if (e,e) not in R: # Validacion de coincidencia de los pares iguales en la relacion
         return False    # Se retorna falso si tras el recorrido no todos los pares iguales se encuentran
 return True # Se retorna true si tras el recorrido todos los pares iguales se encuentran
        
print(A1) 
print(R1)
print(es_reflexiva(A1,R1))  
print(R2)
print(es_reflexiva(A1,R2))           

print("\n");
print("PROBLEMAS # 2"); 

def es_irreflexiva(A, R): # Definicion de la funcion
    for e in A:           # Ciclo para recorrer los elementos
        if (e,e) in R: # Validacion de coincidencia de los pares iguales en la relacion
            return False    # Se retorna false si tras el recorrido se encuentra algun par igual
    return  True # Se retorna True si no se encuentra ningun par igual tras el recorrido

print(A2)
print(R3)
print(R4)
print(es_irreflexiva(A2,R3)) 
print(es_irreflexiva(A2,R4)) 

print("\n");
print("PROBLEMAS # 3");

def es_simetrica(A, R): # Definicion de la funcion
    for i, j in R: # Ciclo para recorrer los elementos
        if (j,i) not in R: # Validacion de coincidencia del par inverso
            return False   # Se retorna false si no se encuentra el par inverso
    return True  # Se retorna true si tras terminar el recorrido se encuentran los pares inversos. 




print(A3)
print(R5) 
print(R6) 

print(es_simetrica(A3,R5))
print(es_simetrica(A3,R6))

print("\n");
print("PROBLEMAS # 4");

def es_asimetrica(A, R): # Definicion de la funcion
    for i, j in R: # Ciclo para recorrer los elementos
        if (j,i) in R: # Validacion de coincidencia del par inverso
            return False # Se retorna false si se encuentra un par inverso
    return True   # Se retorna true si tras el recorrido ningun par inverso fue encontrado  


print(A4)
print(R7)
print(R8)
print(es_asimetrica(A4,R7))
print(es_asimetrica(A4,R8))

print("\n");
print("PROBLEMAS # 5");

def es_antisimetrica(A, R):  # Definicion de la funcion
    for i,j in R:            # Ciclo para recorrer los elementos
        if i!=j and ((i,j) in R and (j,i) not in R): # Validacion de elementos distintos y el par inverso
            return True         # Se retorna true si para elementos distintos no se encuentra el inverso
        if i==j and (i,j) in R: # Se retorna true si los elementos de los pares son iguales
            return True
    return False    # Se retorna false si se encuentra par inverso tras el recorrido


print(A5)
print(R8)
print(R9)
print(es_antisimetrica(A5,R8))
print(es_antisimetrica(A6,R9))


print("\n");
print("PROBLEMAS # 6");   


def es_transitiva(A, R): #Definicion de la funcion
   for a, b in R: # Recorrido de elementos en la relacion
        for c in A: 
            if (b, c) in R: # Validacion de transitividad
                if (a, c) not in R: 
                    return False # Retorno de false tras no encontrar el par que completa la transitividad
   return True # Retorno de true tras los recorridos y encontrar el par que cumple la transitividad



print(A7)
print(R10)
print(R11)

print(es_transitiva(A7,R10))
print(es_transitiva(A7,R11))

print("\n");
print("PROBLEMAS # 7");
# 7a) Validacion de simetria y no transitividad


print(A8)
print(R12)
print(es_simetrica(A8,R12)) 
print(es_transitiva(A8,R12))

# 7b) Validacion de antisimetria y transitividad

print(A9)
print(R13)
print(es_antisimetrica(A9,R13))
print(es_transitiva(A9,R13))


# 7c) Validacion de irreflexibilidad y no transitividad

print(A10)
print(R14)
print(es_irreflexiva(A10,R14))
print(es_transitiva(A10,R14))


# 7d) Validacion de reflexibilidad y no simetria

print(A11)
print(R15)
print(es_reflexiva(A11,R15))
print(es_simetrica(A11,R15))


# 7e) Validacion de simetria y antisimetria

print(A12)
print(R16)
print(es_simetrica(A12, R16))
print(es_antisimetrica(A12, R16))


print("\n");
print("PROBLEMAS # 8");


def dominio(R): # Definicion de la funcion
    dom = set() # Creacion del conjunto dom para guardar el dominio
    for i in R: # Recorrido de los elementos de la relacion
        dom.add(i[0]) # Agregado del primer elemento del par de la relacion al conjunto dom
        
    return dom        
          

print (R1)
print(dominio(R1))

print(R2)
print(dominio(R2))

print("\n");
print("PROBLEMAS # 9");


def codominio(R): # Definicion de la funcion
    cod = set ()  # Creacion del conjunto cod para guardar el codominio
    
    for i in R: # Recorrido de los elementos de la relacion
        cod.add(i[1]) # Agregado del segundo elemento del par de la relacion al conjunto cod
        
    return cod    

print(R9)
print(codominio(R9))
print(R14)
print(codominio(R14))

print("\n");
print("PROBLEMAS # 10");


def funcion_alea(S, T):  
    
    func = set()   # Se crea un conjunto para guardar los pares de la funcion
    
    for i in S:  # Se recorren los elementos del primer conjunto
        if i in T: # Validacion si el elemento del primer conjunto existe en el segundo conjunto
            func.add((i,i)) # Se agrega el elemento a la funcion
    
    return func
            
print(A1)
print(A6)

print(list(funcion_alea(A1,A6)))

print("\n");
print("PROBLEMAS # 11");

def definida_todas_partes(A, R):
    dominio(R) # Uso de la funcion dominio en R
    
    if(dominio(R)==A): # Se valida si el dominio de R es igual al conjunto
        return True # Se retorna true es caso afirmativo
    else:
        return False # Se retorna false en caso negativo
    
print(A13)
print(R17)
print(R18)
print(definida_todas_partes(A13,R17)) 
print(definida_todas_partes(A13,R18))   


A = {1, 2, 3}
R = {(1, 2), (2, 3), (1, 3)}
R1 = {(1, 2), (2, 3), (1, 3), (3, 1)}

print("\n");
print("PROBLEMAS # 12");

def es_uno_a_uno(R):
   val_cod = []  # Lista para guardar los elementos del codominio
   
   for i in R: # Recorrido de los pares de la relacion
       cod = i[1]  # Indicacion de que el codominio esta en la posicion 1 de cada par
       
       if cod in val_cod: # Validacion de existencia del elemento del codominio en la lista
          return False    # De existir se retorna false ya que significa que estaria 
                          # repitiendose en la relacion
       else:
           val_cod.append(cod) # En caso contrario se agrega el elemento del codominio a la lista
       
   return True # Se retorna true tras termino de recorrido y no encontrar repeticiones 
               # de elementos en el codominio
    
print(R18)
print(R19)
print(es_uno_a_uno(R18))
print(es_uno_a_uno(R19))


print("\n");       
print("PROBLEMAS # 13");       

def es_exhaustiva(A, R):
    codominio(R)       # Uso de la funcion codominio en R
    if(codominio(R)==A): # Validacion si el codominio de R es igual a los elementos del conjunto
        return True # Se retorna true en caso positivo
    else:
        return False # Se retorna false en caso negativo

print(A15)
print(R20)
print(R21)

print(es_exhaustiva(A15,R20))
print(es_exhaustiva(A15,R21))

print("\n");
print("PROBLEMAS # 14");

# Problemas # 14

def es_biyectiva(A, R):
    r1 = es_uno_a_uno(R)
    r2 = es_exhaustiva(A, R)
    
    if r1 and r2:
        return True
    else:
        return False

print(A) 
print(R)
print(R1)
print(es_biyectiva(A, R))  # Salida: False
print(es_biyectiva(A, R1))  # Salida: False


print("\n")
print("PROBLEMAS #15")

print(" a) Función uno-a-uno y no exhaustiva:")

def uno_a_uno_no_exhaustiva(R):
    codominio_set = set()
    for _, y in R:
        if y in codominio_set:
            return False
        codominio_set.add(y)
    return True

R = [(1, 2), (2, 3), (3, 4)]  # Ejemplo de conjunto R
print("Conjunto R:", R)
print("Resultado:", uno_a_uno_no_exhaustiva(R))  # Salida: True

print("\n")
print(" b) Función uno-a-uno y no definida en todas partes:")

def uno_a_uno_no_definida(A, R):
    dominio_set = set()
    for x, _ in R:
        if x not in dominio_set:
            dominio_set.add(x)
    return dominio_set != A

A = {1, 2, 3}  # Ejemplo de conjunto A
R = [(1, 2), (2, 3), (4, 5)]  # Ejemplo de conjunto R
print("Conjunto A:", A)
print("Conjunto R:", R)
print("Resultado:", uno_a_uno_no_definida(A, R))  # Salida: False

print("\n")
print("c) Función definida en todas partes y no uno-a-uno:")

def definida_no_uno_a_uno(A, R):
    codominio_set = set()
    for _, y in R:
        if y in codominio_set:
            return True
        codominio_set.add(y)
    return False

R = [(1, 2), (2, 3), (2, 4)]  # Ejemplo de conjunto R
print("Conjunto R:", R)
print("Resultado:", definida_no_uno_a_uno(A, R))  # Salida: False

print("\n")
print("d) Función exhaustiva y no uno-a-uno:")

def exhaustiva_no_uno_a_uno(A, R):
    func = set()
    for i in R:
        func.add(i[1])
    return len(func) == len(A)

R = [(1, 2), (2, 3), (3, 4)]  # Ejemplo de conjunto R
print("Conjunto R:", R)
print("Resultado:", exhaustiva_no_uno_a_uno(A, R))

print("\n")
print(" e) Función biyectiva:")

def biyectiva(A, R):
    func = set()
    for i in R:
        if i[0] not in func:
            func.add(i[0])
        else:
            return False
    return len(func) == len(A) and len(R) == len(A)

R = [(1, 2), (2, 3), (3, 4)]  # Ejemplo de conjunto R
print("Conjunto R:", R)
print("Resultado:", biyectiva(A, R))
