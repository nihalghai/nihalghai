# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 17:15:26 2025

@author: nihal
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/costing")
async def root():
    return {"message": "Sahil"}


from pydantic import BaseModel
import pickle


class Item(BaseModel):
    Square_Footage: int
    


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    
        import pandas as pd
        from sklearn.linear_model import LinearRegression
        df = pd.read_csv(r"C:\Users\nihal\OneDrive\Desktop\Nihal_Study\data\house_price_regression_dataset.csv")
        print (df)

        x = df[["Square_Footage","Num_Bedrooms","Num_Bathrooms","Year_Built","Lot_Size","Garage_Size","Neighborhood_Quality"]]
        y = df[["House_Price"]]

        reg = LinearRegression().fit(x, y)
        
        reg.score(x, y)
        regout = reg.predict([[item.Square_Footage,3,2,2024,2,2,5]])
        print(regout)
        return {"result" : int(regout)}
    
    
    


with open('reg.pkl','wb') as ml:
    pickle.dump(reg,ml)   