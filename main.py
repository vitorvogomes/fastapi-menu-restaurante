from fastapi import FastAPI
from utils.db_querys import create_database
from routes.menu_routes import menu_router
from routes.order_routes import order_router
from routes.booking_routes import booking_router
from routes.review_routes import review_router

app = FastAPI(
    title="Menu Restaurante",
    version="1.0",
    description="API desenvolvida utilizando Python, FastAPI e SQLite3 para permitir que um restaurante consulte ou adicione itens em um Cardápio (Menu), crie pedidos (Orders) dos clientes, salve as reservas (booking) feitas e diponibilize dados sobre os feedbacks (reviews) dos cliente através de avaliações.",
    contact={
        "name": "Vitor Gomes",
        "url": "https://github.com/vitorvogomes",
        "email": "vitorgomes190@gmail.com"
    },
)

# App Routers
app.include_router(menu_router)
app.include_router(order_router)
app.include_router(booking_router)
app.include_router(review_router)

if __name__ == '__main__':
    import uvicorn
    create_database()
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)