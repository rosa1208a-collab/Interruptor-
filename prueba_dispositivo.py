from control.device_adapter import DeviceAdapter

dispositivo = DeviceAdapter()

print("Estado inicial:")
print(dispositivo.consultar_estado())

print("\nEncendiendo la luz...")
print(dispositivo.enviar_orden("ENCENDER"))

print("\nApagando la luz...")
print(dispositivo.enviar_orden("APAGAR"))
