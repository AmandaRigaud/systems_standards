# Interface Command
from abc import ABC, abstractmethod


class Command(ABC):
  @abstractmethod
  def execute(self):
    pass

  @abstractmethod
  def undo(self):
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

# Implementação do Command concreto usando lambda


class LambdaCommand(Command):
  def __init__(self, execute, undo):
    self.execute_func = execute
    self.undo_func = undo

  def execute(self):
    self.execute_func()

  def undo(self):
    self.undo_func()

# Invoker (Controle Remoto)


class RemoteControl:
  def __init__(self):
    self.commands = {}
    self.history = []  # Armazenar o histórico de comandos

  def set_command(self, name, command):
    self.commands[name] = command

  def press_button(self, name):
    if name in self.commands:
      self.commands[name].execute()
      self.history.append(self.commands[name])  # Adiciona ao histórico
    else:
      print(f"Botão '{name}' não configurado.")

  def undo_all(self):
    if self.history:
      print("\nDesfazendo todas as ações...")
      while self.history:
        last_command = self.history.pop()
        last_command.undo()  # Desfaz o último comando
    else:
      print("Nenhuma ação para desfazer.")

# Função para exibir o menu interativo com o estado atual


def display_menu(devices):
  print("\nEstado atual dos dispositivos:")
  for i, device in enumerate(devices, 1):
    print(f"{i} - {device.name}: {device.status()}")
  print("0 - Sair")
  print("9 - Desfazer todas as ações")
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

remote.set_command("Luz da sala - Ligar", LambdaCommand(
    execute=lambda: living_room_light.turn_on(),
    undo=lambda: living_room_light.turn_off()
))
remote.set_command("Luz da sala - Desligar", LambdaCommand(
    execute=lambda: living_room_light.turn_off(),
    undo=lambda: living_room_light.turn_on()
))
remote.set_command("Luz da cozinha - Ligar", LambdaCommand(
    execute=lambda: kitchen_light.turn_on(),
    undo=lambda: kitchen_light.turn_off()
))
remote.set_command("Luz da cozinha - Desligar", LambdaCommand(
    execute=lambda: kitchen_light.turn_off(),
    undo=lambda: kitchen_light.turn_on()
))
remote.set_command("Ventilador de teto - Ligar", LambdaCommand(
    execute=lambda: ceiling_fan.turn_on(),
    undo=lambda: ceiling_fan.turn_off()
))
remote.set_command("Ventilador de teto - Desligar", LambdaCommand(
    execute=lambda: ceiling_fan.turn_off(),
    undo=lambda: ceiling_fan.turn_on()
))
remote.set_command("Porta da garagem - Ligar", LambdaCommand(
    execute=lambda: garage_door.turn_on(),
    undo=lambda: garage_door.turn_off()
))
remote.set_command("Porta da garagem - Desligar", LambdaCommand(
    execute=lambda: garage_door.turn_off(),
    undo=lambda: garage_door.turn_on()
))
remote.set_command("Som - Ligar", LambdaCommand(
    execute=lambda: sound_system.turn_on(),
    undo=lambda: sound_system.turn_off()
))
remote.set_command("Som - Desligar", LambdaCommand(
    execute=lambda: sound_system.turn_off(),
    undo=lambda: sound_system.turn_on()
))

# Menu interativo
while True:
  choice = display_menu(devices)

  if choice == "0":
    print("Saindo...")
    break
  elif choice == "9":
    remote.undo_all()
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
