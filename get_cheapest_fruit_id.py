def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    f=data.split()[1:]
    rows = data.split()[1:]
    price = []
    name = []

    for row in rows:
        price.append(float(row.split(',')[1]))
        name.append(row.split(',')[0])
    
    m=price[0]
    for i in range(len(price)):
        if price[i]<m:
            m=price[i]
    return price.index(m)
data = open('fruits.csv').read()
print(get_cheapest_fruit_id(data))