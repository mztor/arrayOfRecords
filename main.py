class product:
    prodNum = 0
    prodDesc = ""
    qty = 0
    price = 0.0

def createRecord(prodNum, desc, qty, price):
    #creates a new product object and sets the properties according
    #to the parameter values
    p1 = product()
    p1.prodNum = prodNum
    p1.prodDesc= desc
    p1.qty = qty
    p1.price = price
    return p1

def formatProduct(prodObj):
    #formats the details of the product and prints it
    print("Product name:", prodObj.prodDesc)
    print("Quantity remaining:", prodObj.qty)
    print("Price: {:.2f}".format(prodObj.price))

#do this first to learn how to create variables of type product
isRecordNoob = True

if isRecordNoob:
    myFirstProduct = createRecord(5300,"Coke",100,2.50)
    formatProduct(myFirstProduct)
    #create another product with the product number between 5000 and 6000

    #call the formatProduct function and pass it the object you just created

    print(type(myFirstProduct)) # note the data type of myfirstProduct

else:
    products = []
    f = open("data.csv", "r")
    f.readline() #read the heading line
    i = 0
    for line in f:
        products.append(product()) #create a new instance of class product
        vals = line.split(",")
        #write the lines of code that assign the fields of the product object for this particular product


        i += 1
    f.close()

    query = input("Enter a number between 0 and " + str(i-1) + ": ")
    inRange = int(query) < i-1 and int(query) > 0
    while query != "xxx" and inRange:
        formatProduct(products[int(query)])
        query = input("Enter a number between 0 and " + str(i) + ": ")
