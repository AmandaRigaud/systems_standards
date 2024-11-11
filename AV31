# Interface Command
from abc import ABC, abstractmethod


class Command(ABC):
  @abstractmethod
  def execute(self):
    pass


class Device:
  def __init__(self, name):
    self.name = name
    self.on = False

  def turn_on(self):
    if not self.on:
      self.on = True
      print(f"{self.name} ligado.")
    else:
      print(f"{self.name} já está ligado.")

  def turn_off(self):
    if self.on:
      self.on = False
      print(f"{self.name} desligado.")
    else:
      print(f"{self.name} já está desligado.")

  def status(self):
    return "ligado" if self.on else "desligado"


class TurnOnCommand(Command):
  def __init__(self, device):
    self.device = device

  def execute(self):
    self.device.turn_on()


class TurnOffCommand(Command):
  def __init__(self, device):
    self.device = device

  def execute(self):
    self.device.turn_off()

# Invoker (Controle Remoto)


class RemoteControl:
  def __init__(self):
    self.commands = {}

  def set_command(self, name, command):
    self.commands[name] = command

  def press_button(self, name):
    if name in self.commands:
      self.commands[name].execute()
    else:
      print(f"Botão '{name}' não configurado.")

# Função para exibir o menu interativo com o estado atual


def display_menu(devices):
  print("\nEstado atual dos dispositivos:")
  for i, device in enumerate(devices, 1):
    print(f"{i} - {device.name}: {device.status()}")
  print("0 - Sair")
  return input("Escolha o dispositivo que deseja controlar: ")


def display_action(device_name):
  print(f"\nAções disponíveis para {device_name}:")
  print("1 - Ligar")
  print("2 - Desligar")
  return input("Escolha uma ação: ")


# Criando dispositivos
living_room_light = Device("Luz da sala")
kitchen_light = Device("Luz da cozinha")
ceiling_fan = Device("Ventilador de teto da sala")
garage_door = Device("Porta da garagem")
sound_system = Device("Som")

# Lista de dispositivos para exibir no menu
devices = [living_room_light, kitchen_light,
           ceiling_fan, garage_door, sound_system]

# Criando controle remoto
remote = RemoteControl()
remote.set_command("Luz da sala - Ligar", TurnOnCommand(living_room_light))
remote.set_command("Luz da sala - Desligar", TurnOffCommand(living_room_light))
remote.set_command("Luz da cozinha - Ligar", TurnOnCommand(kitchen_light))
remote.set_command("Luz da cozinha - Desligar", TurnOffCommand(kitchen_light))
remote.set_command("Ventilador de teto - Ligar", TurnOnCommand(ceiling_fan))
remote.set_command("Ventilador de teto - Desligar",
                   TurnOffCommand(ceiling_fan))
remote.set_command("Porta da garagem - Ligar", TurnOnCommand(garage_door))
remote.set_command("Porta da garagem - Desligar", TurnOffCommand(garage_door))
remote.set_command("Som - Ligar", TurnOnCommand(sound_system))
remote.set_command("Som - Desligar", TurnOffCommand(sound_system))

# Menu interativo
while True:
  choice = display_menu(devices)

  if choice == "0":
    print("Saindo...")
    break
  else:
    try:
      index = int(choice) - 1
      if 0 <= index < len(devices):
        device = devices[index]
        action = display_action(device.name)

        if action == "1":
          remote.press_button(f"{device.name} - Ligar")
        elif action == "2":
          remote.press_button(f"{device.name} - Desligar")
        else:
          print("Ação inválida. Tente novamente.")
      else:
        print("Opção inválida. Tente novamente.")
    except ValueError:
      print("Opção inválida. Tente novamente.")
