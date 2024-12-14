from address import Address
from mailing import Mailing

to_address = Address("1234", "Springfield", "Elm St", "10", "22")
from_address = Address("7600", "Shelbyville", "Malel st", "5", "18")

mailing = Mailing(to_address, from_address, 1500.5, "TRACK123456")

print(mailing)