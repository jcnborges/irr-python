# jcnborges / irr-python

Olá amigos!

Agradeço pela oportunidade de participar do processo seletivo, espero que gostem do meu programa.

Esse é um repositório público, por isso peço por favor, não compartilhem essa URL com ninguém que não esteja envolvido na minha avalição.

# ambiente de testes

Essa aplicação foi testada em um sistema Ubuntu 18.04 e Docker versão 19.03.6, se você não tiver o Docker faça o seguinte:

sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker

# clone

Baixe meu repositório em seu ambiente de testes:

git clone https://github.com/jcnborges/irr-python.git

# execução

Vá até o diretório raiz da minha aplicação:

docker build --tag irr-python .
docker run --name python-app -p 5000:5000 irr-python
