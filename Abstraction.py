# # step 1
from abc import ABC ,abstractmethod 
# class DeliveryMethod(ABC):
#     @abstractmethod
#     def deliver(self, order_id):
#         pass

# class BikeDelivery(DeliveryMethod):
#     def deliver(self, order_id):
#         print (f"Order {order_id} Delivered by bike")

# bike = BikeDelivery()
# bike.deliver(101)


# #step 2 
# class DeliveryMethod(ABC):
#     @abstractmethod
#     def deliver(self, order_id):
#         pass

# class DroneDeliver(DeliveryMethod):
#     def deliver(self, order_id):
#         print(f"Order {order_id} dropped by drone at your door.")

# class CarDelivery(DeliveryMethod):
#     def deliver(self, order_id):
#         print(f"Order {order_id} brought to your building by car.")

# sending= DroneDeliver()
# sending.deliver(202)
# sending2=CarDelivery()
# sending2.deliver(202)

# ## step 3 Abstract with Constructor
# class DeliveryMethod(ABC):
#     def __init__(self, company_name):
#         self.company_name = company_name

#     @abstractmethod
#     def deliver(self, order_id):
#         pass

# class BikeDelivery(DeliveryMethod):
#     def __init__(self, company_name, ):
#         super().__init__(company_name)

#     def deliver(self, order_id):
#         return f"[{self.company_name}] Order {order_id} — bike delivery."

# class DroneDelivery(DeliveryMethod):
#     def __init__(self, company_name):
#         super().__init__(company_name)

#     def deliver(self, order_id):
#         return f"[{self.company_name}] Order {order_id} — bike delivery."

# sending = BikeDelivery("SpeedRiders")
# print(sending.deliver(303))

# sending1 = DroneDelivery("SkyEx")
# print(sending1.deliver(303))

#step 4. Multiple Abstract Methods
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass

    @abstractmethod
    def get_eta(self):
        pass

class BikeDelivery(DeliveryMethod):
    def deliver(self, order_id):
            print (f"Order {order_id} Delivered by bike")

    def get_eta(self):
            print("30")

class DroneDelivery(DeliveryMethod):
    def deliver(self, order_id):
        print(f"Order {order_id}  Delivered by Drone .")

    def get_eta(self):
            print("15")

Bike_delivery =BikeDelivery()
Bike_delivery.deliver(1)
Bike_delivery.get_eta()

Drone_delivery= DroneDelivery()
Drone_delivery.deliver(2)
Drone_delivery.get_eta()

## step 5 Missing Implementation Error
class DeliveryMethod(ABC):
     @abstractmethod
     def deliver(order_id):
          pass

class BrokenDelivery(DeliveryMethod):
     def deliver(self,order_id):
        print (f"Order {order_id} Delivered by bike")
          
Bike_delivery = BrokenDelivery()
Bike_delivery.deliver(10)

#TypeError: Can't instantiate abstract class BrokenDelivery without an implementation for abstract method 'deliver'










