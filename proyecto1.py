import lifestore_file
import pandas as pd
import numpy as np


products= pd.DataFrame(lifestore_file.lifestore_products,
        columns=["id_product", "name", "price", "category", "stock"])
sales= pd.DataFrame(lifestore_file.lifestore_sales,
        columns=["id_sale", "id_product", "score", "date", "refund"])
searches=pd.DataFrame(lifestore_file.lifestore_searches,
        columns=["id_search", "id_product"])

def prod_vendidos():
    clean=sales[["id_sale","id_product"]]
    id_vendidos = clean.groupby("id_product")["id_sale"].count()
    id_vendidos.sort_values(ascending=False,inplace=True)
    vendidos=id_vendidos.index.tolist()
    print("Los productos más vendidos\n")
    count=1
    for val in vendidos:
       print(str(count)+": "+products.loc[products.id_product==val,"name"].item())
       if(count>49):
           break
       count+=1

def prod_menos_vendidos(cat):
    clean=sales[["id_sale","id_product"]]
    id_vendidos = clean.groupby("id_product")["id_sale"].count()
    id_vendidos.sort_values(ascending=True,inplace=True)
    vendidos=id_vendidos.index.tolist()
    print(f'Los {cat} de menor venta\n')
    count=1
    categorica=products.loc[products.category==cat]
    prod_por_categoria=categorica["id_product"]
    for val in vendidos:
        if(val  in prod_por_categoria):
            item= categorica.loc[categorica["id_product"]==val,"name"].values
            print(str(count)+": "+item)
        if(count>49):
            break
        count+=1

def prod_mas_buscados():
    id_buscados = searches.groupby("id_product")["id_search"].count()
    id_buscados.sort_values(ascending=False,inplace=True)
    buscados=id_buscados.index.tolist()
    print("Los productos más buscados \n")
    count=1
    for val in buscados:
       print(str(count)+": "+products.loc[products.id_product==val,"name"].item())
       if(count>99):
           break
       count+=1
    pass

def prod_menos_buscados(cat):
    id_buscados = searches.groupby("id_product")["id_search"].count()
    id_buscados.sort_values(ascending=True,inplace=True)
    buscados=id_buscados.index.tolist()
    print(f'Los {cat} menos buscados \n')
    count=1
    categorica=products.loc[products.category==cat]
    prod_por_categoria=categorica["id_product"]
    for val in buscados:
        if(val  in prod_por_categoria):
            item= categorica.loc[categorica["id_product"]==val,"name"].values
            print(str(count)+": "+item)
        if(count>99):
            break
        count+=1
    pass
def reseñas():
    no_devoluciones = sales.loc[sales.refund==0]
    ranking1 = no_devoluciones.groupby("id_product")["score"].mean()
    ranking2 = no_devoluciones.groupby("id_product")["score"].mean()
    ranking1.sort_values(ascending=False,inplace=True)
    ranking2.sort_values(ascending=True,inplace=False)
    asc=ranking1.index.tolist()
    desc=ranking2.index.tolist()
    count1=0
    print ("Los productos con mejores reseñas \n")
    for val in asc :
       print(str(count1)+": "+products.loc[products.id_product==val,"name"].item())
       if(count1>19):
           break
       count1+=1
    print("\nLos productos con peores reseñas \n")
    count2=0
    for val in desc :
       print(str(count2)+": "+products.loc[products.id_product==val,"name"].item())
       if(count2>19):
           break
       count2+=1
def ing_ventas():
    id_prod=products["id_product"].tolist()
    prices=products["price"].tolist()
    sales2= sales
    sales2.price=[]
    ing= sales[["id_sale","id_product","date"]]
    ventas= sales.loc[sales.refund==0,["id_sale","id_product","date"]]
    for val in range(0,len(id_prod)+1):
        sales2.loc[sales2.id_product==id_prod[val],"price"]=prices[val]
    #sales2.head()

    pass
def tot_anual():
    pass
def meses_mas_ventas():
    pass
loggedIn=False

user= { "u":"ej", "pwd":"123" }

inputUser = input("Ingresa el usuario :")
pwdUser= input("Ingresa la contraseña :")
if(inputUser == user["u"] and pwdUser==user["pwd"]):
    loggedIn=True
else:
    print("Usuario incorrecto")
while (loggedIn):
    option = input('''Más vendidos : 1 Más buscados:2 , 
    Menos vendidos por categoría : 3, Menos buscados por categoría :4,
     Reseñas de productos:5
    , Ingresos y ventas mensuales : 6, Total anual : 7 ,
     Meses con más ventas: 8, Salir : q \n''')
    
    if(option=="1"):
        prod_vendidos()
    if(option=="2"):
        prod_mas_buscados()
        pass
    if(option=="3"):
        cat = input("Ingresa la categoria : ")
        prod_menos_vendidos(cat)
        pass
    if(option=="4"):
        cat= input("Ingresa la categoría : ")
        prod_menos_buscados(cat)
        pass
    if(option=="5"):
        reseñas()
        pass
    if(option=="6"):
        ing_ventas()
        pass
    if(option=="7"):
        tot_anual()
        pass
    if(option=="8"):
        meses_mas_ventas()
        pass
    if(option=="q"):
        loggedIn=False