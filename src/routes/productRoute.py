from fastapi import APIRouter,HTTPException
from src.utils.utils import get_All_Products, create_product
from src.dtos.productSchema import CreateProductSchema

productRoutes = APIRouter()

@productRoutes.get("/")
def getAllProducts(product_id: int = None):
    products = get_All_Products()
    if not product_id:
     return products
    for product in products:
        if product["id"] == product_id:
            return product
    return HTTPException(status_code=404, detail="Product not found")
    



@productRoutes.get("/{id}")
def getOneProduct(id: int):
    products = get_All_Products()
    for product in products:
        if product["id"] == id:
            return product
        return HTTPException(status_code=404, detail="Product not found")


@productRoutes.post("/create")
def createNewProducts(product: CreateProductSchema):
    product = product.model_dump()
    products = get_All_Products()

    next_id = max([p['id'] for p in products]) + 1
    product['id'] = next_id
    
    products.append(product)
    create_product(products)
    return {'message' : 'Product created successfully'}