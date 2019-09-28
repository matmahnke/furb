caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def validarTexto(txt):
  global caracteres
  for letraInput in txt:
    existeLetra = 0
    for letraCaracteres in caracteres: 
      if(letraInput.upper() == letraCaracteres):
        existeLetra = 1
        break
    if not existeLetra:
      return 0
  return 1

def encriptarTexto(chave, texto):
  global caracteres
  idx_chave = 0
  i = 0
  result = ''
  for letra in texto:
    if idx_chave >= len(chave):
      idx_chave = 0
    if validarTexto(letra):
      indexInput = caracteres.index(letra.upper())
      indexChave = caracteres.index(chave[idx_chave].upper())
      result = result + caracteres[(indexChave + indexInput) % len(caracteres)]
      idx_chave += 1
    else:
      result += letra
    i = i + 1 
  return result

def decriptarTexto(chave, texto):
  global caracteres
  i = 0
  result = ''
  idx_chave = 0
  for letra in texto:
    if idx_chave >= len(chave):
      idx_chave = 0
    if validarTexto(letra):
      indexInput = caracteres.index(letra.upper())
      indexChave = caracteres.index(chave[idx_chave].upper())
      result = result + caracteres[(indexInput - indexChave + len(caracteres)) % len(caracteres)]
      idx_chave += 1
    else:
      result += letra
    i = i + 1 
  return result

def app():
  print("Cifra de Vigenère.")
  txt = input("Informe o texto com letras e números que será operado:")

  texto = txt
  chave = input("Informe a chave:")
  if(validarTexto(chave)):
    resposta = input("Deseja cifrar ou decifrar?\nResponda com C para cifrar ou D para decifrar:");
    result = ''

    if(resposta.upper() == 'C'):
      result = encriptarTexto(chave, texto)
    if(resposta.upper() == 'D'):
      result = decriptarTexto(chave, texto)
    print("Resultado: "+ result)
  else:
    print("Chave inválida")

app()
