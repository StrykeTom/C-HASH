import hashlib
from pystyle import *
import time
import fade

def animate_banner():
    sss = """
     ░█████╗░  ██╗░░██╗░█████╗░░██████╗██╗░░██╗
     ██╔══██╗  ██║░░██║██╔══██╗██╔════╝██║░░██║
     ██║░░╚═╝  ███████║███████║╚█████╗░███████║
     ██║░░██╗  ██╔══██║██╔══██║░╚═══██╗██╔══██║
     ╚█████╔╝  ██║░░██║██║░░██║██████╔╝██║░░██║
     ░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
                    
     https://github.com/StrykeTom  

     Press [ENTER] to continue        
    """
    Anime.Fade(Center.Center(sss), Colors.green_to_blue, Colorate.Vertical, interval=0.050, enter=True)

text = """
     ░█████╗░  ██╗░░██╗░█████╗░░██████╗██╗░░██╗
     ██╔══██╗  ██║░░██║██╔══██╗██╔════╝██║░░██║
     ██║░░╚═╝  ███████║███████║╚█████╗░███████║
     ██║░░██╗  ██╔══██║██╔══██║░╚═══██╗██╔══██║
     ╚█████╔╝  ██║░░██║██║░░██║██████╔╝██║░░██║
     ░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
                    
     https://github.com/StrykeTom  
     
     Press [ENTER] to continue        
"""

animate_banner2 = fade.purplepink(text)

def crackear_hash(hash_a_crackear, diccionario):
    algoritmos = [
        'md5', 'halfmd5', 'doublemd5', 'ntlm', 'ripemd160', 'ripemd256', 'ripemd320',
        'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'whirlpool', 'mysql5', 'keccak-224',
        'keccak-256', 'keccak-384', 'keccak-512', 'sha3-224', 'sha3-256', 'sha3-384', 'sha3-512',
        'shake128', 'shake256'
    ]

    try:
        with open(diccionario, 'r', encoding='utf-8') as archivo_diccionario:
            for palabra in archivo_diccionario:
                palabra = palabra.strip()

                for algoritmo in algoritmos:
                    try:
                        hash_generado = getattr(hashlib, algoritmo)(palabra.encode()).hexdigest()
                    except AttributeError:
                        continue

                    if hash_generado == hash_a_crackear:
                        return palabra, algoritmo

    except FileNotFoundError:
        return f"Error: Archivo de diccionario '{diccionario}' no encontrado"
    except ValueError:
        return "Error: Hash no válido"
    except Exception as e:
        return f"Error desconocido: {e}"

    return "No encontré el maldito Hash"

animate_banner()
print(animate_banner2)

archivo_diccionario = input("Ingresa el nombre del archivo de diccionario (incluyendo extensión): ")
hash_a_crackear = input("Ingresa el Hash: ")

resultado = crackear_hash(hash_a_crackear, archivo_diccionario)
if isinstance(resultado, tuple):
    palabra, algoritmo = resultado
    print(f"Cracking exitoso con algoritmo {algoritmo}:", palabra)
else:
    print("Error:", resultado)
