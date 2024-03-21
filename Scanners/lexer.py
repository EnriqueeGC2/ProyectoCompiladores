import os
import ply.lex as lex
from html import escape

open ('bitacora_errores.html', 'w').close()

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
    'SIMBOLOS',
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

tokensReconocidos = []
tabla_simbolos = {}
posicion_anterior = 0

def agregar_simbolo(token, tipo, valor, linea, posicion, rol, tamano=None, visibilidad=None, ambito=None):
    tabla_simbolos[valor] = {
        'token': token,
        'tipo': tipo,
        'valor': valor,
        'linea': linea,
        'posicion': posicion,
        'rol': rol,
        'tamano': tamano,
        'visibilidad': visibilidad,
        'ambito': ambito
    }
# Expresión regular para palabras clave 
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tipos de datos
def t_ENTERO(t):
    r'Entero'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Tipos de datos', len(t.value))
    return t

def t_CARACTER(t):
    r'Caracter'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Tipos de datos')
    return t

def t_LOGICO(t):
    r'Logico'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Tipos de datos')
    return t

def t_REAL(t):
    r'Real'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Tipos de datos')
    return t
# Palabras reservadas
def t_ALGORITMO(t):
    r'Algoritmo'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_FIN(t):
    r'Fin(Algoritmo|Para|Segun|Mientras|Funcion)'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t  

def t_DEFINIR(t):
    r'Definir'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Acciones Secuenciales')
    return t

def t_COMO(t):
    r'Como'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Acciones Secuenciales')
    return t

def t_ESCRIBIR(t):
    r'Escribir'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Acciones Secuenciales')
    return t

def t_LEER(t):
    r'Leer'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Acciones Secuenciales')
    return t

# Funciones y estructuras de control
def t_PARA(t):
    r'Para'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_FUNCION(t):
    r'Funcion'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_MIENTRAS(t):
    r'Mientras'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_SEGUN(t):
    r'Segun'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_DE_OTRO_MODO(t):
    r'De_Otro_Modo'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_HACER(t):
    r'Hacer'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_SI(t):
    r'Si'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_SINO(t):
    r'Sino'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_ENTONCES(t):
    r'Entonces'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Estructuras de control')
    return t

def t_COMENTARIO(t):
    r'Comentario'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Acciones Secuenciales')
    return t

# OPERADORES ALGEBAICOS
def t_MAS(t):
    r'\+'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

def t_MENOS(t):
    r'-'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

def t_POR(t):
    r'\*'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

def t_DIVIDIDO(t):
    r'/'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

def t_POTENCIA(t):
    r'Potencia'
    t.value = '**'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

def t_RESIDUO(t):
    r'%'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Algebaicos')
    return t

# OPERADORES RELACIONALES
def t_ES_MAYOR_QUE(t):
    r'Es_Mayor_Que' 
    t.value = '>'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

def t_ES_MENOR_QUE(t):
    r'Es_Menor_Que'
    t.value = '<'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

def t_ES_IGUAL_QUE(t):
    r'Es_Igual_Que'
    t.value = '=='
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

def t_ES_MAYOR_O_IGUAL_QUE(t):
    r'Es_Mayor_O_Igual_Que'
    t.value = '>='
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

def t_ES_MENOR_O_IGUAL_QUE(t):
    r'Es_Menor_O_Igual_Que'
    t.value = '<='
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

def t_ES_DISTINTO_QUE(t):
    r'Es_Distinto_Que'
    t.value = '!='
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Relacionales')
    return t

#OPERADORES LOGICOS
def t_Y(t):
    r'Y'
    t.value = '&&' # Reemplazar el token por el valor '&&'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Lógicos')
    return t

def t_O(t):
    r'O'
    t.value = '||' # Reemplazar el token por el valor '||'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Lógicos')
    return t

def t_NO(t):
    r'NO'
    t.value = '!' # Reemplazar el token por el valor '!'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Operadores Lógicos')
    return t

#Simbolos y caracteres
def t_A_COM(t):
    r'A_Com'
    t.value = "'" # Reemplazar el token por el valor '/'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_C_COM(t):
    r'C_Com'
    t.value = "'" # Reemplazar el token por el valor '/'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_A_PAR(t):
    r'\('
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_C_PAR(t):
    r'\)'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_DOS_P(t):
    r'Dos_P'
    t.value = ':'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_P_COM(t):
    r'P_Com'
    t.value = ';'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_COMA(t):
    r'Coma'
    t.value = ','
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_VARIABLES(t):
    #r'[a-zA-Z]+'
    r'[a-z]+|(A-Z)+' # Expresión regular para variables
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Identificadores')
    return t

def t_CADENAS(t):
    r'[a-zA-Z_][_a-zA-Z]*' # Expresión regular para cadenas'
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Cadenas de Texto')
    return t  

def t_NUMERO(t):
    r'\d*\.?\d+' # Expresión regular para números decimales y enteros
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Números')
    return t

def t_SIMBOLOS(t):
    r'[\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]' # Expresión regular para símbolos
    '''
    \x21-\x2F -> coincide con los símbolos del código ASCII desde el signo de exclamación hasta la barra inclinada hacia adelante.
    \x3A-\x40 -> coincide con los símbolos del código ASCII desde los dos puntos hasta la arroba.
    \x5B-\x60 -> coincide con los símbolos del código ASCII desde el corchete izquierdo hasta el acento grave.
    \x7B-\x7E -> coincide con los símbolos del código ASCII desde la llave izquierda hasta la tilde.
    '''
    agregar_simbolo(t.value, t.type, t.value, t.lineno, t.lexpos, 'Símbolos')

# Función de manejo de errores
def t_error(t):
    with open('bitacora_errores.html', 'a') as file:
        file.write(f"<p> Carácter no reconocido: ' {t.value[0]} ' | Linea: {t.lineno} | Posición: {t.lexpos}<p>\n")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()

# Leer el archivo de fuente
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()

def escribir_tabla_simbolos_html():
    with open("tabla_simbolos.html", "w") as archivo_html:
        # Escribir el encabezado del HTML
        archivo_html.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Tabla de Símbolos</title>\n</head>\n<body>\n")

        # Escribir el encabezado de la tabla
        archivo_html.write("<table border='1'>\n<tr>\n<th>Token</th>\n<th>Tipo</th>\n<th>Valor</th>\n<th>Línea</th>\n<th>Posición</th>\n<th>Rol</th>\n<th>Ámbito</th>\n<th>Visibilidad</th>\n<th>Tamaño</th>\n</tr>\n")

        # Iterar sobre los símbolos y escribir cada fila de la tabla
        for token, atributos in tabla_simbolos.items():
            archivo_html.write("<tr>\n")
            archivo_html.write(f"<td>{token}</td>\n")
            archivo_html.write(f"<td>{atributos['tipo']}</td>\n")
            archivo_html.write(f"<td>{atributos['valor']}</td>\n")
            archivo_html.write(f"<td>{atributos['linea']}</td>\n")
            archivo_html.write(f"<td>{atributos['posicion']}</td>\n")
            archivo_html.write(f"<td>{atributos['rol']}</td>\n")
            archivo_html.write(f"<td>{atributos['ambito']}</td>\n")
            archivo_html.write(f"<td>{atributos['visibilidad']}</td>\n")
            archivo_html.write(f"<td>{atributos['tamano']}</td>\n")
            archivo_html.write("</tr>\n")
        
        # Cerrar la tabla y el cuerpo del HTML
        archivo_html.write("</table>\n</body>\n</html>")

    with open("bitacora_tokens.html", "w") as archivo_html:
        # Escribir el encabezado del HTML
        archivo_html.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Bitácora de Tokens</title>\n</head>\n<body>\n")
        archivo_html.write("<h2>Bitácora de Tokens:</h2>\n")
        for token, atributos in tabla_simbolos.items():
            archivo_html.write(f"<p>Token: ' {token} ' <br>| Tipo: ' {atributos['tipo']} ' <br>| Valor: ' {atributos['valor']} ' <br>| Línea: ' {atributos['linea']} ' <br>| Posición: ' {atributos['posicion']} '</p>\n")
        archivo_html.write("</body>\n</html>")

# Ejemplo de uso
if __name__ == '__main__':
    nombre_archivo = 'ejemplo.txt'
    codigo_fuente = leer_archivo(nombre_archivo)

    # Alimentar el analizador léxico con el código fuente
    lexer.input(codigo_fuente)

    while True:
        tok = lexer.token()
        if not tok:
            break  # No hay más tokens
        tokensReconocidos.append(tok)

    escribir_tabla_simbolos_html()

    print("Tabla de símbolos generada en tabla_simbolos.html")