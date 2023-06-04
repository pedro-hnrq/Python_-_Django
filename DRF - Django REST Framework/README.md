<h1 align="center"> Django REST Framework - DRF</h1>

<h2 align="center"> Prévia <h2>

![DRF](https://github.com/pedro-hnrq/Python_-_Django/assets/74242717/c7dff0fd-c827-4755-87f7-71350d6d9c6d)

  
  
<h3>Objetivo</h3>

<h6 align="justify">No uso do Django REST Framework (DRF) e suas principais funcionalidades. Busco dominar através de projeto que consiste em gerencie os cursos e avaliações das disciplinas. Dessa forma, aplicado os conceitos essenciais do DRF, como manipulação de solicitações e respostas HTTP, serialização de dados, criação de endpoints GET, POST, PUT e DELETE, configuração de rotas com routers, utilização de viewsets e mixins, criação de ações personalizadas, autenticação e autorização com tokens, controle de permissões, controle de taxa de acesso (throttling), personalização de validações e testes unitários com PyTest. Dessa forma, com intuito de aplicar essas habilidades em projetos reais, visando a criação de APIs RESTful robustas e eficientes. Pretendo utilizar o DRF para desenvolver APIs que forneçam uma interface de comunicação segura, escalável e de alto desempenho entre o front-end e o back-end de um sistema.</h6>

 
<h4>Etapas</h4>
  <h5>Para que o usuário execute o DRF na sua máquina, siga os seguintes passos:</h5>
  
<ol>
<li>Clone este repositório em sua máquina utilizando o seguinte comando no terminal:</li> 
 
```
git clone git@github.com:pedro-hnrq/Python_-_Django.git
```  
   
 <li>Vá ao diretório do Django REST Framework.</li>
    
 <li>Verifique se já na sua máquina tenha o Python instalado, se tiver crie e logo em seguida o ambiente virtual. </li>
  
<li>Instale as dependências do projeto através do arquivo requirements.txt: </li>
  
```
pip install -r requirements.txt
```

<li>Crie um superusuário para acessar a área administrativa:</li>
  
```
python3 manage.py createsuperuser
```
  
<li>Execute as migrações do banco de dados:</li>
  
```
python3 manage.py migrate
```
  
<li>Execute servidor:</li>  
  
```
python3 manage.py runserver
```
  
<li>Acesse o endereço http://localhost:8000/admin e faça login com as credenciais do superusuário criado anteriormente.</li>
  
<li>Para acessar a API, utilize o endereço http://localhost:8000/api/v1/ para a versão 1 da API e http://localhost:8000/api/v2/ para a versão 2 da API. As rotas disponíveis podem ser encontradas nos arquivos cursos/urls.py e escola/urls.py.</li> 
  
<li>Observação: usei o IDE do Pycharm juntamente com o Programa Insomnia para realiza as requisição HTTP (GET, POST, PUT, DELETE e Token), mas poderá utilizar o IDE do Visual Studio Code com a extensão Thunder Client ou programa do Postman.</li>
</ol>
