from
from router.receita import receita_router
from fastapi import FastAPI



app=FastAPI()

app.include_router(receita_router)
app
@app.get('/')
async def test():
    return "nadas"

