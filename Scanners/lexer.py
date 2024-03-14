import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    #RESERVADAS
    'FIN',
    'ALGORITMO',
    'CADENAS',
    'LETRAS',
    'NUMERO',
    'ESCRIBIR',
    'LEER',
    'PARA',
    'FUNCION',
    'MIENTRAS',
    'SEGUN',
    'HACER',
    'SI',
    'SINO',
    'DE_OTRO_MODO'
    'ENTONCES',
    'ES_MAYOR_QUE',
    'ES_MENOR_QUE',
    'ES_IGUAL_QUE',
    'ES_MAYOR_O_IGUAL_QUE',
    'ES_MENOR_O_IGUAL_QUE',
    'ES_DISTINTO_QUE',
    #OPERADORES LOGICOS
    'Y',
    'O',
    'NO',
    #OPERADORES ARITMETICOS
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'ELEVADO_A',
    'RESIDUO',
    #FUNCIONES
    'CONVERTIRATEXTO',
    'CONVERTIRANUMERO',
    'COMENTARIO'
)

# Expresión regular para palabras clave
#t_ALGORITMO = r'Algoritmo'  
t_ignore = ' \n'
def t_ESCRIBIR(t):
    r'Escribir'
    return t

def t_LEER(t):
    r'Leer'
    return t

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

def t_HACER(t):
    r'Hacer'
    return t

def t_SI(t):
    r'Si'
    return t

def t_SINO(t):
    r'Sino'
    return t

def t_DE_OTRO_MODO(t):
    r'De otro modo'
    return t

def t_ENTONCES(t):
    r'Entonces'
    return t

def t_ALGORITMO(t):
    r'Algoritmo'
    return t

def t_FIN(t):
    r'Fin(Algoritmo|Para|Segun|Mientras|Funcion)'
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

def t_ELEVADO_A(t):
    r'\^'
    return t

def t_RESIDUO(t):
    r'%'
    return t

def t_ES_MAYOR_QUE(t):
    r'>'
    return t

def t_ES_MENOR_QUE(t):
    r'<'
    return t

def t_ES_IGUAL_QUE(t):
    r'=='
    return t

def t_ES_MAYOR_O_IGUAL_QUE(t):
    r'>='
    return t

def t_ES_MENOR_O_IGUAL_QUE(t):
    r'<='
    return t

def t_ES_DISTINTO_QUE(t):
    r'!='
    return t

def t_LETRAS(t):
    r'[a-zA-Z]+'
    return t

def t_CADENAS(t):
    r'[a-zA-Z_][a-zA-Z]*'
    if t.value.lower() == 'algoritmo':
        t.type = 'ALGORITMO'  # Cambia el tipo de token
    return t  

def t_NUMERO(t):
    r'\d*\.?\d+' # Expresión regular para números decimales y enteros
    return t

# Función de manejo de errores
def t_error(t):
    print(f"\nCarácter no reconocido: '{t.value[0]}'")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

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
