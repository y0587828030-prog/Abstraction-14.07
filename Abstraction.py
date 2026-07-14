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


#step 2 
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

class DroneDeliver(DeliveryMethod):
    def deliver(self, order_id):
        print(f"Order {order_id} dropped by drone at your door.")

class CarDelivery(DeliveryMethod):
    def deliver(self, order_id):
        print(f"Order {order_id} brought to your building by car.")

sending= DroneDeliver()
sending.deliver(202)
sending2=CarDelivery()
sending2.deliver(202)










# # step 2
# class DeliveryMethod(ABC):

#     @abstractmethod
#     def deliver(self,order_id):
#         pass

# class DroneDelivery (DeliveryMethod):
     
#      def deliver(self,order_id):
#         print (f"{order_id} dropped by dron at your door")

        
# class CarDelivery (DeliveryMethod):
     
#      def deliver(self,order_id):
#         print (f"{order_id} brought to your building by car")

# car = CarDelivery()
# car.deliver(202)
# drone = DroneDelivery()
# drone.deliver(202