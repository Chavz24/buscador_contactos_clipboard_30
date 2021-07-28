#regex para el numero
import  re


buscar_numero = re.compile(r'''(
(\(\d{3}\)|\d{3})?                              #codigo area
(\s|\.|-)?                                      #separador
(\d{3})                                         #primeros tres digitos numero principal
(\s|\.|-)                                       #segundo separador
(\d{4})                                         #ultimos cuatro digitos
(\s*(ext.|x.|ext|x))?(\s*\d{,5})?)'''           # extension
, (re.VERBOSE | re.I))                          #re.VERBOSE ignora espacio en blanco
                                                #re.I ve mayusculas y minusculas por igual

