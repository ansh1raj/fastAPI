
import json
file_path = "src/data/products.json"

def get_All_Products():
    with open(file_path, "r") as p:
        return json.load(p)
    
def create_product(products: list):
    with open(file_path, "w") as p:
        json.dump(products, p)