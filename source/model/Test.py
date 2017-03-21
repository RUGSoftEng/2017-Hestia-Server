from model.Action import Action
from model.Device import Device
from model.DeviceDAO import DeviceDAO

light = Device("Light")
light.addAction(Action("On/Off"))
light.addAction(Action("Color"))

lock = Device("Lock")
lock.addAction(Action("Open/Close"))

DOA = DeviceDAO()
DOA.add(light)
DOA.add(lock)

print(DOA)