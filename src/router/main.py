from router.despesa import despesa_router
from router.receita import receita_router
from fastapi import FastAPI



app=FastAPI()

app.include_router(receita_router)
app.include_router(despesa_router)



