"""
Name: {นางสาวสุธาทิพย์ ทองใบใหญ่}
SID: {364211760027}
Group: {MIT221}
"""

 # class Relations - Dependency

from datetime import date

class Customer:
     def __init__(self,cusid,name):
         self.cusid = cusid
         self.name = name

     def customer_info(self):
         return f'CusID: {self.cusid} Customer name: {self.name}'

class Order:
    def __init__(self,orderid,date,customer,total):
        self.orderid = orderid
        self.date = date
        self.customer = customer
        self.total = total

    def order_info(self):
        print("Order description:")
        print(f'\tCustomer info: {self.customer.customer_info()}')
        print(f'\tDate: {self.date}')
        print(f'\tTotel cost: {self.total}')

#
cus1 = Customer("CUS001","Sutatip Tongbaiyai")

order1 = Order("ORDER001",date.today(),cus1,15000)
order1.order_info()
