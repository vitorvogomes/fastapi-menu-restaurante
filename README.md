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
- Forneçe uma lista dos pedidos feitos, incluindo detalhes como número do pedido, itens, status e total.

###### POST "/orders" --> CREATE ORDER
- Permite que os clientes realizem pedidos, especificando os itens do cardápio que desejam e a quantidade.

###### GET "/orders/{order_num}" --> GET ORDER BY NUM
- Permite que os clientes obtenham informações detalhadas sobre um pedido específico.

###### GET "/orders/{order_num}" --> DELETE ORDER
- Permite que os clientes obtenham informações detalhadas sobre um pedido específico.

###### PUT "/orders/{order_num}/satus" --> UPDATE ORDER STATUS
- Permite que os funcionários do restaurante atualizem o status de um pedido, "Pendente", "Confirmado", "Retirada", "Entreue" ou "Cancelado".


#### ENDPOINTS PARA BOOKING

###### GET "/booking" --> GET BOOKINGS LIST
- Forneçe uma lista das reservas feitas, incluindo detalhes como data, hora, número de pessoas e status.

###### POST "/booking" --> CREATE BOOKING
- Permite que os clientes façam reservas para mesas no restaurante, especificando a data, hora e número de pessoas.

###### GET "/booking/{booking_id}" --> GET BOOKING BY ID
- Permite que os clientes obtenham informações detalhadas sobre uma reserva específica.

###### PUT "/booking/{booking_id}" --> UPDATE BOOKING STATUS
- Permite que o restaurante atualize o status de uma reserva, como "aguardando", "confirmada" ou "cancelada." 


#### ENDPOINTS PARA REVIEWS

###### GET "/reviews" --> GET REVIEWS LIST
- Forneçe uma lista de avaliações feitas por clientes, incluindo detalhes como classificação, comentários e data.

###### POST "/reviews" --> CREATE REVIEW
- Permite que os clientes avaliem o restaurante e deixem comentários sobre sua experiência.


#### ENDPOINTS PARA CLIENTS
CREATE, LIST, UPDATE



## POSTMAN COLLECTION :book:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/23458410-b9b8524c-891a-4304-abde-2c9a1563fef7?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D23458410-b9b8524c-891a-4304-abde-2c9a1563fef7%26entityType%3Dcollection%26workspaceId%3Defb2f2ab-d95a-495f-bc2b-ef74d93aa7a9)



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
| nps_score            |    [str]
| review_date          |    [DateTime]
| order_num (FK)       |    [str]
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


