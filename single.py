from user import User
from chat_history import ChatHistory
User_one = User()
User_two = User()
User_one.send_message('Hello')
User_two.send_message('Hello, id like to place an order')
User_one.send_message('Of course what would you like to order?')
User_two.send_message('what do you have on the menu?')
User_one.send_message('we have a few items avaliable such as pancakes and sausage')
ChatHistory.display_history()
