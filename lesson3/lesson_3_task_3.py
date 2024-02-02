from address import Address
from mailing import Mailing

to_address = Address("123456", "lipetsk", "Pervaya", "1", "12")
from_address = Address("654321", "Voronezh", "Vtoraya", "33", "47")

mailing_instance = Mailing(to_address, from_address, 250, "123ABC")

print(f"Отправление {mailing_instance.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} "
      f"в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {mailing_instance.cost} рублей.")
