async def check_date(list_,date,description):
    for i in list_:
        if i.data.month == date and i.descricao == description:
            return False
    return True