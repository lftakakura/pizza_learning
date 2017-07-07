# Pizza Learning 2 #

## Sobre ##

As apresentaçes estão no diretório 0 e os códigos estão no diretório 0/adorocinema
Todos os código estão escritos em python 3.x. 
<b>link_extractor.py</b> e <b>movie_extractor.py</b> são os crawlers e <b>predict.py</b> é o código do modelo de predição.
Nos arquivos <b>movies.csv</b> e <b>movies_test.csv</b>, já temos um dataset processado para treinamento do modelo.

## Como rodar ##

### requisitos ###
- python 3.x
- virtualenv (opcional)
- pip3

### Instalação (ubuntu) ###
1) <b>sudo apt-get install python3</b>
2) <b>sudo apt-get install pip3</b>
3) <b>sudo apt-get install virtualenv</b>

De dentro do diretório 0/adorocinema faça:

4) crie um ambiente virtual para instalar todas as dependências do programa e rodá-lo:
   <b>virtualenv -p python3 env_pizza_learning</b>
5) inicialize o virtualenv
   <b>source env_pizza_learning/bin/activate</b>
6) instale as dependências do programa:
   <b>pip install -r requirements.txt</b>

### Executando ##
Execute o comando <b>python predict.py</b>

O modelo será treinado utilizando o arquivo <b>movies_test.csv</b>. Após o treinamento, o programa ficará em  um loop infinito para receber input textual e categroizá-lo.

Para sair do virtualenv basta executar <b>deactivate</b>
