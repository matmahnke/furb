import re

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
texto = '';
chave = '';

def validarTexto(txt):
  valido = 0;
  for letraInput in txt:
    existeLetra = 0;
    for letraCaracteres in caracteres: 
      if(letraInput == letraCaracteres):
        existeLetra = 1;
    if(existeLetra):
      valido = 1;
  return valido;

def encriptarTexto():
  i = 0;
  result = '';
  for letra in texto:
    indexInput = caracteres.index(letra)
    indexChave = caracteres.index(chave[i])
    result = result + caracteres[(indexChave + indexInput) % len(caracteres)]
    i = i + 1;
  return result;

def decriptarTexto():
  i = 0;
  result = '';
  for letra in texto:
    indexInput = caracteres.index(letra)
    indexChave = caracteres.index(chave[i])
    result = result + caracteres[(indexInput - indexChave + len(caracteres)) % len(caracteres)]
  return result;

print("Cifra de Vigenère.")
txt = input("Informe um texto com letras e números:")

if(validarTexto(txt)):
  texto = txt;
  chave = input("Informe a chave:");
  if(validarTexto(chave)):
    resposta = input("Deseja cifrar ou decifrar?\nResponda com C para cifrar ou D para decifrar:");
    result = '';

    if(resposta.upper() == 'C'):
      result = encriptarTexto();
    if(resposta.upper() == 'D'):
      result = decriptarTexto();

    print("Resultado: "+ result);


else:
  print("Texto inválido");