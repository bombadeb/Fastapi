from pydantic import BaseModel


class Blog(BaseModel):
    types: str
    grid_file: str
    pole_file: str
    critical_distances: str