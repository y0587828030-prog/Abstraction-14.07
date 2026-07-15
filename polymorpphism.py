## 1. Device Activation
class Device:
    def __init__(self, name):
        self.name = name

    def activate(self):
        print(f"Device {self.name} is now on.")

class SmartTV(Device):
    def __init__(self, name):
        super().__init__(name)

    def activate(self):
        print(f"TV {self.name} is playing the home screen.")

class SmartSpeaker(Device):
    def __init__(self, name):
        super().__init__(name)

        print(f"Speaker {self.name} is ready to play music.")

tv = SmartTV("Samsung")
tv.activate()

speaker = SmartSpeaker("Echo")
speaker.activate()