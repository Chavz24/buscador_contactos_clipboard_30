#regex para el email

import re

buscar_email=re.compile(r'''(
[a-z0-9&$#!?.,<>_%+-]+      #nombre usuario
@                           #signo arroba
[a-z0-9.-]+                 # el dominio
\.([a-z0-9.-]{2,4}))'''     #un punto seguido algo
,(re.I|re.VERBOSE))

