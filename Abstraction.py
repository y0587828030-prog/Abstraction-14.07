# step 1
from abc import ABC ,abstractmethod 
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

class BikeDelivery(DeliveryMethod):
    def deliver(self, order_id):
        print (f"Order {order_id} Delivered by bike")

bike = BikeDelivery()
bike.deliver(101)











