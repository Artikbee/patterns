class Light:
    def turn_on(self):
        print("Свет включен.")

    def turn_off(self):
        print("Свет выключен.")


class AirConditioner:
    def start(self):
        print("Кондиционер включен.")

    def stop(self):
        print("Кондиционер выключен.")


class DeviceAdapter:
    def __init__(self, device, on_method, off_method):
        self.device = device
        self.on_method = on_method
        self.off_method = off_method

    def switch_on(self):
        getattr(self.device, self.on_method)()

    def switch_off(self):
        getattr(self.device, self.off_method)()


def client_code(device):
    device.switch_on()
    device.switch_off()


if __name__ == "__main__":
    light = Light()
    air_conditioner = AirConditioner()

    light_adapter = DeviceAdapter(light, "turn_on", "turn_off")
    client_code(light_adapter)

    air_conditioner_adapter = DeviceAdapter(air_conditioner, "start", "stop")
    client_code(air_conditioner_adapter)
