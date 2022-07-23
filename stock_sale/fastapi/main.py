import copy
from fastapi import FastAPI, Response, status, HTTPException

stock_list = [{"name": "test", "amount": 100}, {"name": "aiute", "amount": 10}]

def find_stock(name=None):
    return_dict = {}
    if name is None:
        return_dict = sorted(stock_list, key=lambda x:x['name'])
        return return_dict
    for i in stock_list:
        if i['name'] == name:
            return_dict = copy.copy(i)
            return return_dict
    else:
        return_dict = {f"name": name, "amount": int(0)}
        return return_dict

@app.get("/posts/{name}", status_code=status.HTTP_201_CREATED)
def get_post(id: int, response: Response):
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
#        response.status_code = status.HTTP_404_NOT_FOUND
#        return {'message': "ERROR"}

@app.delete("/v1/stocks")
def delete_stock():
    clear

curl http://localhost:8000/

print (find_stock("test"))