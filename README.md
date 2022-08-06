# Curso Engenharia de Dados AWS 

### Módulo 0 - Setup (Mac OS)

```shell
# Instalando o Python e o PIP no Mac OS https://python.org.br/instalacao-mac/
brew install python3
python3 -m pip install --upgrade pip
# Instalando e habilitando o Virtual Env https://docs.python.org/pt-br/3/library/venv.html
pip3 install virtualenv
source .venv/bin/activate
# Instalando pacotes necessários para os Módulos
pip3 install requests
pip3 install pandas lxml
pip3 install ipython
```
### Módulo 1 - Fundamentos

##### Script para rodar sem o `ipython`
```shell
python main.py 'http://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil'
```