class Product:
    def __init__(self, name, category, supply_price, sale_price, quantity_sold):
        self.name = name
        self.category = category
        self.supply_price = supply_price
        self.sale_price = sale_price
        self.quantity_sold = quantity_sold

    def benefit(self):
        return (self.sale_price - self.supply_price) * self.quantity_sold


def collect():
    name = input("Enter toy name: ")
    category = input("Enter toy category: ")
    supply_price = float(input("Enter supply price: "))
    sale_price = float(input("Enter sale price: "))
    quantity_sold = int(input("Enter quantity sold: "))
    return Product(name, category, supply_price, sale_price, quantity_sold)


def get_total_benefit(toys):
    total = 0
    for toy in toys:
        total += toy.benefit()
    return total


def get_most_sold(toys):
    most_sold = toys[0]
    for toy in toys:
        if toy.quantity_sold > most_sold.quantity_sold:
            most_sold = toy
    return most_sold.name


def get_best_product(toys):
    best_product = toys[0]
    for toy in toys:
        if toy.benefit() > best_product.benefit():
            best_product = toy
    return best_product.name


def get_worst_product(toys):
    worst_product = toys[0]
    for toy in toys:
        if toy.benefit() / toy.quantity_sold < worst_product.benefit() / worst_product.quantity_sold:
            worst_product = toy
    return worst_product.name


def main():
    toys = []
    num_toys = int(input("How many toys do you want to enter? "))
    for i in range(num_toys):
        toys.append(collect())

    print("Total Benefit:", get_total_benefit(toys))
    print("Most Sold Product:", get_most_sold(toys))
    print("Best Product:", get_best_product(toys))
    print("Worst Product:", get_worst_product(toys))


main()
