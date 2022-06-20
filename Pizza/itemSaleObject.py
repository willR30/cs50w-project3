#se creara un objeto a partir de esta clase a fin de crear el item de la orden
class itemSaleObject:
    def __init__(self, id_product,amount,details):
        self.id_product=id_product
        self.amount=amount
        self.details=details