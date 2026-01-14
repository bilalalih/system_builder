from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def process_file(name:str = "default"): # QUery parameter name passed using ?
    processed_name = name.upper()
    return{"name": name, "uppercase":processed_name}