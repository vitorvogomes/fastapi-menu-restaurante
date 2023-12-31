# API para Pedidos de um Restaurante :fork_and_knife:


## DESCRIÇÃO DO PROJETO :pencil2:

API desenvolvida utilizando Python, FastAPI e SQLite3 para permitir que um restaurante crie um Cardápio (Menu), crie pedidos (Orders) dos clientes, salve as reservas (booking) feitas e diponibilize dados sobre os feedbacks (reviews) dos cliente através de avaliações. Um banco de dados feito em SQLite3 para armazenar e disponibilizar as informações sobre o restaurante.



## TECNOLOGIAS :bulb:

1. [Python]
2. [FastAPI]
3. [SQLite3]

### Dependências instaladas

- Acessar documento "requirements.txt"



## INICIALIZAÇÃO DO SERVIDOR :computer:

- Criar ambiente virtual
```sh
$python -m venv .venv
```

- Inicializar o ambiente virtual
```sh
$source .venv/Scripts/activate "ou" $source .venv/bin/activate
```

- Download das dependencias do projeto
```sh
$pip install -r requirements.txt
```

- Executar o arquivo "main.py"
```sh
$python main.py
```

## POSTMAN COLLECTION :book:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/23458410-b9b8524c-891a-4304-abde-2c9a1563fef7?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D23458410-b9b8524c-891a-4304-abde-2c9a1563fef7%26entityType%3Dcollection%26workspaceId%3Defb2f2ab-d95a-495f-bc2b-ef74d93aa7a9)


#### DOCUMENTAÇÃO

- Acessar [LINK] "{{BASE_URL}}/docs"


#### ENDPOINTS PARA MENU

###### POST "/menu" --> CREATE ITEM
- Permite que o restaurante adicione itens no cardápio.

###### GET "/menu" --> GET MENU ITEMS
- Permite que os clientes obtenham uma lista de itens do Cardápio.

###### GET "/menu/{item_id}" --> GET ITEM BY ID
- Forneçe informações detalhadas sobre um item específico do cardápio.

###### PUT "/menu/{item_id}" --> UPDATE ITEM BY ID
- Permite que um item específico do cardápio seja atualizado.

###### DELETE "/menu/{item_id}" --> DELETE ITEM BY ID
- Permite que um item específico do cardápio seja excluido.

###### GET "/categories" --> GET MENU CATEGORIES
- Forneçe informações sobre as categorias disponíveis no cardápio.

###### GET "/categories/{category_name}/items" --> GET ITEM BY CATEGORY
- Forneçe itens do cardápio de acordo com uma categoria específica.


#### ENDPOINTS PARA ORDERS

###### GET "/orders" --> GET ORDERS LIST
- Forneçe uma lista dos pedidos, incluindo detalhes como número do pedido, itens, status, total, e-mail do cliente.
- Possui parâmetros de consulta para filtrar através da data ou do status do pedido.

###### POST "/orders" --> CREATE ORDER
- Permite que os clientes realizem pedidos, especificando os itens do cardápio que desejam e a quantidade.

###### GET "/orders/{order_num}" --> GET ORDER BY NUM
- Permite que os clientes obtenham informações detalhadas sobre um pedido específico.

###### GET "/orders/{order_num}" --> DELETE ORDER
- Permite que os clientes obtenham informações detalhadas sobre um pedido específico.

###### PUT "/orders/{order_num}/satus" --> UPDATE ORDER STATUS
- Permite que os funcionários do restaurante atualizem o status de um pedido, "Pendente", "Confirmado", "Retirada", "Entregue" ou "Cancelado".


#### ENDPOINTS PARA BOOKING

###### GET "/booking" --> GET BOOKING LIST
- Forneçe uma lista das reservas feitas, incluindo detalhes como data, número de pessoas e status.
- Possui parâmetros de consulta para filtrar através da data marcada ou do status da reserva.

###### POST "/booking" --> CREATE BOOKING
- Permite que os clientes façam reservas para mesas no restaurante, especificando a data, e número de pessoas.
- Se o número máximo de pessoas do estabelecimento for ultrapassado no dia, não será permitido criar uma nova reserva.

###### PUT "/booking/{booking_id}" --> UPDATE BOOKING STATUS
- Permite que o restaurante atualize o status de uma reserva, como "Solicitado", "Confirmado", "Finalizado" ou "Cancelado".
- O status é atualizado através do parâmetro de consulta "new_status".


#### ENDPOINTS PARA REVIEWS

###### GET "/reviews" --> GET REVIEWS LIST
- Forneçe uma lista de avaliações feitas por clientes, incluindo detalhes como uma nota de classificação, comentários e data.
- Possui parâmetros de consulta para filtrar através da data da avaliação ou da nota de classificação.

###### POST "/reviews" --> CREATE REVIEW
- Permite que os clientes avaliem o restaurante e deixem comentários sobre sua experiência.


#### ENDPOINTS PARA CLIENTS
###### GET "/clients" --> GET CLIENTS LIST
- Forneçe uma lista de clientes cadastrados, incluindo detalhes como nome, e-mail, endereço e forma de pagamento.
- Possui parâmetros de consulta para filtrar através do nome.

###### POST "/clients" --> CREATE CLIENT
- Permite que o restaurante cadastre os dados do cliente.

###### PUT "/clients/{client_email}" --> UPDATE CLIENT DATA
- Permite que o restaurante atualize o endereço ou a forma de pagamento de um cliente.

###### DELETE "/clients/{client_email}" --> DELETE CLIENT DATA
- Permite que o restaurante apague um cliente específico através do e-mail.



## RESUMO TABELAS SQLITE3 :page_facing_up:

#### Informações sobre as itens do cardápio
  
|       MenuData       |     
|----------------------|    
| item_id (PK)         |    [uuid]
| item_name            |    [str]
| item_description     |    [str]
| item_price           |    [float]
| category_name        |    [str]


#### Informações sobre pedidos feitos
   
|      OrdersData      |    
|----------------------|    
| order_id (PK)        |    [uuid]
| order_num            |    [str]
| order_items          |    [str]
| order_status         |    [str]
| order_total          |    [float]
| order_date           |    [DateTime]*
| client_email (FK)    |    [str]*


#### Informações sobre reservas 
   
|      BookingData     |     
|----------------------|    
| booking_id (PK)      |    [uuid]
| people_num           |    [int]
| booking_status       |    [str]
| booking_date         |    [DateTime]
| client_email (FK)    |    [str]*



#### Informações sobre avaliações feitas
  
|     ReviewsData      |     
|----------------------|    
| review_id (PK)       |    [uuid]
| review_description   |    [str]
| review_score         |    [str]
| review_date          |    [DateTime]
| client_email (FK)    |    [str]*


#### Informações sobre clientes

|      ClientData      |    
|----------------------|
| client_id (PK)       |    [uuid]*
| client_name          |    [str]*
| client_email         |    [str]*
| adress               |    [str]*
| postal_code          |    [str]*
| payment_type         |    [str]*


