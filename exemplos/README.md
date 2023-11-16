# UML


# Exercícios STARUML

Adaptado de:
```
O´Neill, H. (2004). Fundamental do UML. FCA, Editora de Informática.
```
## Casos de Uso
### Bolsa de Emprego

Pretende-se desenvolver um sistema de informação para uma bolsa de emprego com os seguintes atores:
- Administrador: O administrador representa a pessoa ou entidade responsável pela gestão 
do sistema desenvolvido, que é responsável pela validação dos registos dos empregadores e 
dos candidatos, fazendo a atribuição de um login e  de uma password, sendo também o 
responsável pela remoção dos anúncios com validade expirada.;
- Empregador: O empregador representa a pessoa que disponibiliza anúncios de oferta de emprego, aos candidatos à procura de emprego;
- Candidato: O candidato representa o utilizador que procura anúncios que satisfaçam os seus interesses.
Os casos de uso necessários são:
- Colocar anúncios de oferta de emprego: Corresponde a uma ação realizada por um empregador, que depois de autenticado poderá preencher um formulário correspondente a um anúncio de oferta de emprego.
- Pesquisar candidatos: Este caso de uso consiste na pesquisa, por parte dos empregadores, de candidatos registados na Bolsa de Emprego, de acordo com diferentes critérios.
- Alterar dados de registo: Os candidatos e os empregadores, depois de registados na Bolsa de Emprego, poderão alterar os seus dados de identificação, como por exemplo, contacto, email, morada, etc. Os candidatos poderão fazer alteração do seu Curriculum Vitae.
- Fazer registo: Este caso de uso corresponde à introdução dos dados que permitam identificar os diferentes utilizadores do sistema, empresa ou candidato. Para o caso de candidatos, o registo deverá incluir um formulário com dados relativos ao seu Curriculum Vitae.
- Candidatura a anúncio: Como o próprio nome do caso de uso sugere, a candidatura a anúncio refere-se à ação por parte dos candidatos a emprego, de envio de um mail com os seus dados (dados pessoais, CV, referências, etc...) para o empregador.
- Validar Registo: Este é um caso de uso do administrador da Bolsa de Emprego, que depois de efetuado um registo de candidato ou de empregador, deverá verificar os dados introduzidos, e em caso de validação deverá enviar um login e uma password que lhes permita o acesso à aplicação.
- Consultar anúncios: Os candidatos registados na Bolsa de Emprego poderão consultar os diferentes anúncios disponíveis, de acordo com diferentes critérios pré-definidos, como, funções a desempenhar, local de trabalho, habilitações, etc...
- Autenticação: Como visível na figura 1, quase todos os casos de uso definidos implicam a autenticação dos utilizadores do sistema, empregadores ou candidatos, ou seja, a introdução do login e da respetiva password, que receberam aquando do registo.
- Remover anúncios: Este caso de uso é da responsabilidade do administrador do sistema, consistindo na remoção, automática (requisito não mínimo) ou não, dos anúncios presentes no sítio com validade expirada(valor a especificar).
- Notificar: Embora este caso de uso tenha sido especificado como requisito não-mínimo, pretende representar a notificação que deverá ser efetuada pelo administrador do sistema, aos candidatos, caso seja introduzido algum anúncio da sua área de interesse, e aos empregadores, caso algum candidato introduza um curriculum compatível com à área dos empregadores registados. De notar, que tal como referido em requisitos não-mínimos, esta notificação poderá ser efetuada automaticamente, sem intervenção direta do administrador do sistema.
 

Resolução: [Bolsa de Emprego](01.bolsaEmprego/)

### Restaurante Fast-food
#### Atores
- Sistema telefone: sistema que permite os clientes contactem com o restaurante para comer no restaurante ou fazer takeway
- Sistema Internet: permite realizar as encomendas online para comer no restaurante ou fazer takeway
- Cliente: Pode realizar e consultar encomendas no balcão, telefone ou internet. Pode consultar o catálogo de produtos e promoções.
- Empregado de balcão: Receber encomendas, reservar mesas, consultar encomendas e receção pedido de encomendas
- Gestor: Alterar estado encomendas
- Sistema Central de Gestão: Integra informação de várias fontes. Suporta consulta do catálogo de produtos, encomendas realizadas, envio encomendas


#### Casos de Uso
##### Receção pedido de encomendas

- Efetuar encomendas (balcão e internet)
- Consultar catálogo de produtos
- Consultar promoções
- Reservar mesas
- Enviar encomendas
- Consultar encomendas
- Alterar estado encomendas

Resolução: [Encomendas restaurante](02.restaurante/)

### Encomenda bibliteca


Resolução: [Encomendas biblioteca](03.biblioteca/)

## Diagrama de classes
### Encomendas de produtos
- Definir o diagrama de classe de um site de vendas online de material informático;
- Um cliente pode realizar várias encomendas, onde cada encomenda pode conter vários produtos e a respetiva quantidade encomendada;
- Construa um diagrama de classes simplificado, considerando só os elementos fundamentais;

### Encomendas de livros
- Uma biblioteca possui dois tipos de publicações, livros e revistas. Um interessado em requisitar uma publicação tem que preencher uma ficha de empréstimo, preenchendo a cota (conjunto de letras e número para identificar) e o título. Se for um livro tem que preencher os autores. 
- O requisitante tem que pagar uma caução. Disponibilizar o telefone de contacto e morada
- As publicações novas são catalogadas por um responsável pela catalogação, onde é definida a área de conhecimento. Nos livros tem que ser registado o número de identificação internacional, ISBN e periodicidade nas revistas.

Resolução: [Diagramas de classes](04.diagramaClasses/)



