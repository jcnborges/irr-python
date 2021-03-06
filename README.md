# jcnborges / irr-python

Olá amigos!

Agradeço pela oportunidade de participar do processo seletivo, espero que gostem do meu programa.

Esse é um repositório público, por isso, eu peço que não compartilhem essa URL com ninguém mais além de vocês.

Um abraço!

Júlio César

# ambiente de testes

Essa aplicação foi testada em um sistema Ubuntu 18.04 e Docker versão 19.03.6, se você não tiver o Docker faça o seguinte:

```
sudo apt-get install docker.io

sudo systemctl start docker

sudo systemctl enable docker
```

# clone

Baixe meu repositório em seu ambiente de testes:

```
git clone https://github.com/jcnborges/irr-python.git
```

# carregamento

Eu já deixei a imagem pronta, então basta carregar no container de vocês!

Infelizmente ela é maior que o limite de arquivos do git então a deixei disponível para download em: https://drive.google.com/open?id=1BMxXNH8IlSjcktpxH2TW258zdBfFNVqw

Na pasta onde você baixou o arquivo, execute o comando:

```
sudo docker load < irr-python-julio-cesar-bs-nardelli.tar.gz
```

# build

Caso você não tenha conseguido baixar minha imagem, pode construí-la em seu ambiente. O projeto já possui um arquivo ***Dockerfile*** configurado. Na pasta raiz do projeto execute o comando:

```
sudo docker build --tag irr-python-julio-cesar-bs-nardelli .
```

# execução

Depois que a imagem estiver instalada, execute-a em um container. No meu teste, usei um container chamado ***python-app***, certifique-se de que esse nome não esteja em uso, caso esteja, pode mudar o nome.

```
sudo docker run --name python-app -p 5000:5000 irr-python-julio-cesar-bs-nardelli
```
# testes unitários

Caso você queira executar os testes unitários, na pasta raiz do projeto execute o comando:

```
python -m unittest -v unit.py
```