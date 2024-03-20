import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    # Tipos de datos
    'ENTERO',
    'CARACTER',
    'LOGICO',
    'REAL',
    # Palabra reservadas 
    'DEFINIR',
    'COMO',
    'FIN',
    'ALGORITMO',
    'CADENAS',
    'VARIABLES',
    'NUMERO',
    # Funciones y estructuras de control
    'ESCRIBIR',
    'LEER',
    'PARA',
    'FUNCION',
    'MIENTRAS',
    'SEGUN',
    'HACER',
    'SI',
    'SINO',
    'DE_OTRO_MODO',
    'ENTONCES',
    'CONVERTIRATEXTO',
    'CONVERTIRANUMERO',
    'COMENTARIO',
    #OPERADORES RELACIONALES
    'ES_MAYOR_QUE',
    'ES_MENOR_QUE',
    'ES_IGUAL_QUE',
    'ES_MAYOR_O_IGUAL_QUE',
    'ES_MENOR_O_IGUAL_QUE',
    'ES_DISTINTO_QUE',
    #OPERADORES ARITMETICOS
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'POTENCIA',
    'RESIDUO',
    #OPERADORES LOGICOS
    'Y',
    'O',
    'NO',
    #SIMBOLOS Y CARACTERES
    'A_COM',
    'C_COM',
    'A_PAR',
    'C_PAR',
    'DOS_P',
    'P_COM',
    'COMA',
)

# Expresión regular para palabras clave 

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tipos de datos
def t_ENTERO(t):
    r'Entero'
    return t

def t_CARACTER(t):
    r'Caracter'
    return t

def t_LOGICO(t):
    r'Logico'
    return t

def t_REAL(t):
    r'Real'
    return t
# Palabras reservadas
def t_ALGORITMO(t):
    r'Algoritmo'
    return t

def t_FIN(t):
    r'Fin(Algoritmo|Para|Segun|Mientras|Funcion)'
    return t  

def t_DEFINIR(t):
    r'Definir'
    return t

def t_COMO(t):
    r'Como'
    return t

def t_ESCRIBIR(t):
    r'Escribir'
    return t

def t_LEER(t):
    r'Leer'
    return t

# Funciones y estructuras de control
def t_PARA(t):
    r'Para'
    return t

def t_FUNCION(t):
    r'Funcion'
    return t

def t_MIENTRAS(t):
    r'Mientras'
    return t

def t_SEGUN(t):
    r'Segun'
    return t

def t_DE_OTRO_MODO(t):
    r'De_Otro_Modo'
    return t

def t_HACER(t):
    r'Hacer'
    return t

def t_SI(t):
    r'Si'
    return t

def t_SINO(t):
    r'Sino'
    return t

def t_ENTONCES(t):
    r'Entonces'
    return t

def t_COMENTARIO(t):
    r'Comentario'
    return t

# OPERADORES 
def t_MAS(t):
    r'\+'
    return t

def t_MENOS(t):
    r'-'
    return t

def t_POR(t):
    r'\*'
    return t

def t_DIVIDIDO(t):
    r'/'
    return t

def t_POTENCIA(t):
    r'Potencia'
    t.value = '**'
    return t

def t_RESIDUO(t):
    r'%'
    return t

def t_ES_MAYOR_QUE(t):
    r'Es_Mayor_Que' 
    t.value = '>'
    return t

def t_ES_MENOR_QUE(t):
    r'Es_Menor_Que'
    return t

def t_ES_IGUAL_QUE(t):
    r'Es_Igual_Que'
    t.value = '=='
    return t

def t_ES_MAYOR_O_IGUAL_QUE(t):
    r'Es_Mayor_O_Igual_Que'
    t.value = '>='
    return t

def t_ES_MENOR_O_IGUAL_QUE(t):
    r'Es_Menor_O_Igual_Que'
    t.value = '<='
    return t

def t_ES_DISTINTO_QUE(t):
    r'Es_Distinto_Que'
    t.value = '!='
    return t

#OPERADORES LOGICOS
def t_Y(t):
    r'Y'
    t.value = '&&' # Reemplazar el token por el valor '&&'
    return t

def t_O(t):
    r'O'
    t.value = '||' # Reemplazar el token por el valor '||'
    return t

def t_NO(t):
    r'NO'
    t.value = '!' # Reemplazar el token por el valor '!'
    return t

#Simbolos y caracteres
def t_A_COM(t):
    r'A_Com'
    t.value = "'" # Reemplazar el token por el valor '/'
    return t

def t_C_COM(t):
    r'C_Com'
    t.value = "'" # Reemplazar el token por el valor '/'
    return t

def t_A_PAR(t):
    r'\('
    return t

def t_C_PAR(t):
    r'\)'
    return t

def t_DOS_P(t):
    r'Dos_P'
    t.value = ':'
    return t

def t_P_COM(t):
    r'P_Com'
    t.value = ';'
    return t

def t_COMA(t):
    r'Coma'
    t.value = ','
    return t

def t_VARIABLES(t):
    #r'[a-zA-Z]+'
    r'[a-z]+|(A-Z)+' # Expresión regular para variables
    return t

def t_CADENAS(t):
    r'[a-zA-Z_][_a-zA-Z]*' # Expresión regular para cadenas'
    return t  

def t_NUMERO(t):
    r'\d*\.?\d+' # Expresión regular para números decimales y enteros
    return t

# Función de manejo de errores
def t_error(t):
    print(f"\nCarácter no reconocido: '{t.value[0]}' | Linea: {t.lineno} | Posición: {t.lexpos}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex(outputdir='.', optimize=False)

# Leer el archivo de fuente
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

# Ejemplo de uso
if __name__ == '__main__':
    nombre_archivo = 'ejemplo.txt'
    codigo_fuente = leer_archivo(nombre_archivo)

    # Alimentar el analizador léxico con el código fuente
    lexer.input(codigo_fuente)

    # Obtener los tokens
    for tokens in lexer:
        print('\nToken: ',tokens.type, '| Valor: ',tokens.value, '| Linea: ',tokens.lineno, '| Posicion: ',tokens.lexpos)
