# este archivo usa los regex anteriores para buscer matches en el clipboard

import pyperclip
from regex_busca_emails import*
from regex_busca_numero_telefono import*

texto=str(pyperclip.paste())

matches=[]

for grupos in buscar_numero.findall(texto):
    numero_telefono='-'.join([grupos[1],grupos[3],grupos[5]])
    if grupos[8]!='':
        numero_telefono+= " x" + grupos[8]
    matches.append(numero_telefono)
for grupos in buscar_email.findall(texto):
    matches.append(grupos[0])

