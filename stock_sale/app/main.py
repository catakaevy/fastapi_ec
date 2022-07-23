from fastapi.params import Body
from fastapi.responses import PlainTextResponse
from typing import List, Optional, Union
from fastapi import FastAPI
from pydantic import BaseModel, conint, constr, confloat, ValidationError, validator
import copy
import math

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def get_AWS():
    return 'AWS'

#Type check functions
error_pattern = {"message": "ERROR"}

class Stock(BaseModel):
    name: constr(strict=True)
    amount: conint(strict=True, gt=0)
#    @validator('amount')
#    def amount_is_int(cls, v):
#        if type(v) is not int:
#            raise ValueError('Amount must be int')
#        return v
#class Config:
#        error_msg_templates = {"message": "ERROR"}


class None_Stock(BaseModel):
    name: constr(strict=True)
    amount: Optional[None] = int(1)

stock_list = [{"name": "", "amount": None}]

class Sale(BaseModel):
    name: str
    amount: Optional[int] = int(1)
    price: Optional[float]

sale_list = [{"name": "", "amount": None, "price": None}]
sale_num_list = []

#Type check functions
error_pattern = {"message": "ERROR"}

#(1) 在庫の更新、作成
@app.post("/v1/stocks")
def add_stock(new_stock: Stock):
#    try:
#        Stock(new_stock)
#    except ValidationError as e:
#        raise e
#    if new_stock["amount"]==None:
#        none_stock = None_Stock()
#        none_stock.set(new_stock)
#    else:
#        stock = Stock()
#        stock.set(new_stock)
    stock_dict = new_stock.dict()
    stock_list.append(stock_dict)
    return stock_dict


#(2) 在庫チェック
def find_stock(name=None):
    return_dict = {}
    if name is None:
        return_dict = sorted(stock_list, key=lambda x:x['name'])
        if return_dict != None:
            return_dict.pop(0)
        return return_dict
    for i in stock_list:
        if i['name'] == name:
            return_dict = copy.copy(i)
            return return_dict
    else:
        return_dict = {f"name": name, "amount": int(0)}
        return return_dict

@app.get("/v1/stocks")
def get_stock():
    stock = find_stock()
    return stock

@app.get("/v1/stocks/{name}")
def get_stock(name):
    stock = find_stock(name)
    return stock

#(3)販売
#might need to consider how to remove stock_num at the same time
@app.post("/v1/sales")
def add_sale(new_sale: Sale):
   sale_dict = new_sale.dict()
   if sale_dict['price'] != None:
       for i in stock_list:
        if i['name'] == sale_dict['name']:
            same_stock = i
            same_stock['amount'] = same_stock['amount'] - sale_dict['amount']
       sale_list.append(sale_dict)
       sale_num = sale_dict['price']*sale_dict['amount']
       sale_num_list.append(sale_num)
   return sale_dict

#(4)売り上げチェック
@app.get("/v1/sales")
def get_sales():
    total_salenum = sum(sale_num_list)
    total_salenum = float(total_salenum)
    if total_salenum.is_integer() == True:
        total_salenum = f'{total_salenum:.02f}'
        return {f"sales": total_salenum}
    else:
        total_salenum = math.ceil(total_salenum)
        total_salenum = total_salenum / 100
        return {f"sales": total_salenum}

#(5)全削除
@app.delete("/v1/stocks")
def delete_stocks():
    stock_list.clear()
    sale_list.clear()
    sale_num_list.clear()
    return "Deleted!"
