# AMAZON BUYER AND VENDER

def send_email():
    welcome_text = welcome_amazon_greet(False, "rakesh")
    print("send_email ith message::" + welcome_text)
def welcome_amazon_greet(is_buyer, name):
    print("hello", '' + name)
    if is_buyer:
        return "welcome to amazon buyer family"
    else:
        return "welcome to amazon vender family"
send_email()