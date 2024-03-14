from pydantic import BaseModel, Field



class TVModel(BaseModel):
    id: str
    data: dict

class DataModel(BaseModel):
    id: str
    name: str
    price: dict
