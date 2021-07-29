

from buscar_match_en_clipboard import *

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print("Elementos copiados en el clipboard")
    print('\n'.join(matches))
else:
    print('No se encontraron elementos que copiar')
