class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0

def log_transaction(self, order,store_num):
    self.transaction_count += 1
    self.daily_sales += order.price
    file = open("Restaurant.txt", "a")
    file.write(f"Transaction Count: {self.transaction_count}\nDish: {order.dish_name} (${order.price}.00)\nLocation Number:{store_num}\nTotal Sales: $(self.daily_sales).00\n\n")   
    file.close()

logger = Logger()
