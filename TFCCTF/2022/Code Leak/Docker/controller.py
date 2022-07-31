import random

class Controller:
  def __init__(self, name):
    self.name = name
    self.money = 0
    self.works = 0
    self.encrypted_flag = 'Q(\x02\x90ÃÂ´Ã\x87kÂª;NÃÃ¼\n\x83Â¢ÃIÂ©Ã¶gUÃ¤Â¾Z4\x1eÃ¾ÃIv\x03Ã¦x\x90{~'


  def buy_flag(self):
    if self.money < 1337:
      return f"{self.name} does not have enough money"
    
    flag = []

    for x in self.encrypted_flag:
      flag.append(ord(x))
      
    random.seed(133773211629381620483)
    
    for i in range(len(flag)):
      flag[i] ^= random.randint(0, 256)

    flag_ascii = []

    for x in flag:
      flag_ascii.append(chr(x))

    return ''.join(flag_ascii)

  def check_balance(self):
    return f"{self.name} has ${self.money}"

  def work(self):
    self.works += 1

    if self.works > 6:
      return f"{self.name} worked too much"

    earn = random.randint(5, 10)
    self.money += earn

    return f"{self.name} worked and earned ${earn}"

  def buy_hint(self):
    if self.money < 30:
      return f"{self.name} does not have enough money"

    self.money -= 30

    return "Never waste your money on useless things"


