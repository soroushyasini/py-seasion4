
products = []
def read_database():
    data = open("C:/Users/soroush/Desktop/Adobe.Reader.11.0.10/database.txt","r")
    for line in data:
        result=line.split(",")
        shop_list={"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(shop_list)
        print(result)
read_database()
def show_menu():
    global munu
    munu = input("""
    hello Dear Customer ! please tell us how can we help you , Press ENTER and then input your choice.
     to add a new thing,   --> 1
     to search the shop    --> 2
     to edit your list     --> 3
     to see your list      --> 4
     to buy something      --> 5
     to remove something   --> 6
     to exit               --> 0 
    """)
    global choice
    choice=int(input("enter your choice: "))

def add():
    new_id=input("id: ")
    new_name=input("name: ")
    new_price=input("price: ")
    new_count=input("count: ")
    new_list={"id":new_id,"name":new_name,"price":new_price,"count":new_count}
    products.append(new_list)
    print(new_list)
def search():
    search_prd = input("enter product ID or Its Name : ")
    for i in products:
        if i["id"] == search_prd or i["name"]== search_prd :
            print(i)
            break
    else:
        print("The Product You searching for, is not Found.")
def delete():
    del_prd=input("enter product ID or Its Name : ")
    for i in products:
       if i["id"] == del_prd or i["name"]== del_prd :    
          products.remove(i)
          print("The Product you selected, has been deleted.")
          break
def show_list():
     #print("id\nname\tprice\tcount")
     for i in products:
         print(i["id"],"\t",i["name"],"\t",i["price"],i["count"])
###############     
def edit():

    edit = int(input(""" edit name  ---> 1
                         edit price ---> 2
                         edit count ---> 3
    
    """))
    if edit == 1 :
        old_name = input("input the old name of product : ")
        new_name = input("input the new name : ")
        for product in products:
            if product["id"] == old_name or product["name"]== old_name : 
                product["name"]=new_name
                print(product)
                print("name has been changed.")
                break 
    if edit == 2: 
        name_p =input("enter your product name or its ID : ")
        new_price=int(input("pleas inter new price : "))
        for i in products:
            if i["id"] == name_p or i["name"]== name_p : 
                i["price"]=new_price
                print(i)
                print("price is changed")
                break 

    if edit == 3:
        name_c = input("enter your product name or its ID : ")
        new_count=int(input("pleas inter new count : "))
        for i in products:
            if i["id"] == idkey5 or i["name"]== name_c : 
                i["count"]=new_count
                print(i)
                print("the count has been changed . ")
                break 
      
def buy():
    buy=[]
    while True:
        product_buy=input("enter product name or its ID : ")
        for i in products:
            if i["id"] == product_buy or i["name"] == product_buy:
                print(i)
                amount=int(input("how much do you want to buy now ? : "))
                mojody=int(i['count'])
                gheymat=int(i['price'])
    
                if mojody==0:
                    print("there is no selected product.")
                elif amount >= mojody:
                    print("you picked up more than limit.")
                elif amount <= mojody:
                    sum = amount*gheymat
                    print(sum)
                    buy.append(sum)
                    print(buy)
                
        else:
            print("are you sure you choose a  correct pruduct ? ")



while True:
    show_menu()
    if choice==1:
        add()
    if choice==2: 
        search()
    if choice==3: 
        edit()
    if choice==4:
        show_list()
    if choice==5: 
        buy()
    if choice==6: 
        delete()
    if choice==0:
        opr=input("""
        if you want to save the changes, press y
        other wise press n 
         : """)
        if opr=="y":
            data = open("store.txt","w")
            for i in products:
                data.write(i["id"]+i["name"]+i["price"]+i["count"])
                data.write("\n")
                data.close() 
            exit()  
        else:
            exit()
        
    
    else:
        print("pleas select another")