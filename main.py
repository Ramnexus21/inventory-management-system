from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
import database_models
from models import Product
from sqlalchemy.orm import Session 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)



database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Hello world"

# list of products with 4 products like phones, laptops, pens, tables
products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db = SessionLocal()
    count = db.query(database_models.ProductDB).count()
    if count == 0:
        for product in products:
                db.add(database_models.ProductDB(**product.model_dump()))
        db.commit()

init_db()






@app.get("/products/")
def get_all_products(db: Session  =Depends(get_db)):
    db_products = db.query(database_models.ProductDB).all()
    return db_products


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session =Depends(get_db)):
    db_product = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == product_id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}

@app.post("/products/")
def create_product(product: Product,db: Session =Depends(get_db)):
    db.add(database_models.ProductDB(**product.model_dump()))
    db.commit()
    return {"message": "Product created successfully", "product": product}


@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product, db: Session =Depends(get_db)):
    db_product = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {"message": "Product updated successfully", "product": product}
    else:
        return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session =Depends(get_db)):
    db_product = db.query(database_models.ProductDB).filter(database_models.ProductDB.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        return {"error": "Product not found"}