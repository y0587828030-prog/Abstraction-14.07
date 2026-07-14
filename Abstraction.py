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

##step 6. Static Delivery Fee Calculator
class DeliveryFee:
     @staticmethod
     def calculate(distance_km, rate_per_km):
          return distance_km * rate_per_km

     @staticmethod
     def with_surcharge(base_fee, surcharge_percent):
          return base_fee * (1 + surcharge_percent / 100)

     @staticmethod
     def is_free(distance_km):
          return distance_km <= 2.0

Calculation = print(DeliveryFee.calculate(5, 3.0))    
Calculation_with_addition = print(DeliveryFee.with_surcharge(15.0, 10))
Distance_calculation = print(DeliveryFee.is_free(1.5))


#step 7. Abstract + Static Together
class DeliveryMethod(ABC):
     @abstractmethod
     def deliver(order_id):
        pass
     def get_eta(): 
        pass

class WalkingDelivery(DeliveryMethod):
     def deliver(order_id):
        return order_id
     
     def get_eta(self): 
        return 60   
     
class ExpressDelivery(DeliveryMethod):
     def deliver(order_id):
        return order_id
     
     def get_eta(self): 
        return 10

class DeliveryHelper():
     @staticmethod
     def faster(d1, d2):
          if d1.get_eta() < d2.get_eta():
               return d1
          else:
               return d2

Standard_delivery= WalkingDelivery()
express_delivery = ExpressDelivery()

Calculation = DeliveryHelper().faster(Standard_delivery,express_delivery)
print(f"Faster option{Calculation.__class__.__name__}")

## step 8 Notification Abstract Class
class Notifier(ABC):
     @abstractmethod
     def send(self, recipient, message):
          pass

class PushNotifier(Notifier):
    def send(self, recipient, message):
         print(f"push to {recipient}: {message}")

class WhatsAppNotifier(Notifier):
    def send(self, recipient, message):
         print(f"WhatsApp to {recipient}: {message}")

class InAppNotifier(Notifier):
    def send(self, recipient, message):
         print(f"In-app banner for{recipient}: {message}")

messages_list =[PushNotifier(),WhatsAppNotifier(),InAppNotifier()]
for message in messages_list:
     message.send("customer_42", "Your order is on the way!")