import requests
import pandas as pd
import sys

url = 'http://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'


r = requests.get(url, verify=False)

r