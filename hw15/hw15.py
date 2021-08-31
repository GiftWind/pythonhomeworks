# Написать класс router.
# Должен иметь методы добавить/удалить/вывести список ip address.
# Должен иметь методы добавить/удалить/вывести список ip routes.

# Есть маршруты к непосредственно-подключенным сетям:
# если у устройства есть ip-adress 192.168.5.14/24 на интерфейсе eth1,
# значит у него должен быть маршрут:
# к сети 192.168.5.0/24 через eth1 или через 192.168.5.14.

# Если мы хотим добавить маршрут к какой-нибудь удаленной сети,
# то надо проверять доступен ли gateway.

# Например мы можем добавить маршрут к 172.16.0.0/16 через gateway
# 192.168.5.132, только если у нас уже есть маршрут до 192.168.5.132.

# Если же мы попытаемся добавить маршрут до какой-либо сети через gateway,
# до которого у нас пока еще нет маршрута, то должен вылетать exception.

# Например:
# Добавляем ip-address 192.168.5.14/24 eth1.
# Добавляем маршрут до 172.16.0.0/16 через 192.168.5.1 - ok.
# Добавляем маршрут до 172.24.0.0/16 через 192.168.8.1 - exception.
# Добавляем маршрут до 172.24.0.0/16 через 172.16.8.1 - ok.

# Итого - 1 интерфейс и 3 маршрута в таблице.
import ipaddress
class Router():
    """
    Router representation.
    Attributes:
        addresses: dictionary representing router interfaces
        routes: dictionary representing route table
    """
    def __init__(self):
        """Inits router with empty route table and no interfaces"""
        self.routes = {}
        self.addresses = {}
    
    def add_address(self, address, interface):
        """Adds interface with assigned address to addresses dictionary.
        Adds route to directly connected network.
        Args:
            address: string containing IP address in CIDR notation
            interface: string containing interface name (i.e. "eth01")
        """
        self.addresses[address] = interface
        # Calculating address of network containing the interface address 
        connectednetwork = ipaddress.ip_interface(address).network
        # Add directly connected network to route table
        self.routes[str(connectednetwork)] = address.split('/')[0]
    def delete_address(self, address):
        """ Deletes address from addresses dictionary.
        Deletes routes to networks.
        Args:
            address: string containing IP address in CIDR notation
        """
        self.addresses.pop(address)
        # The routes through the deleted gateway are not accessible now.
        for route in self.routes:
            if self.routes[route] == address:
                self.routes.pop(route)

    def show_addresses(self):
        """Shows interfaces with addresses"""
        for address in self.addresses:
            print(f'{address} - {self.addresses[address]}')

    def add_route(self, destination, gateway):
        """Adds route to network
        Args: 
            destination: destination network address in CIDR notation
            gateway: address of gateway
        Raises:
            ValueError: gateway is unreachable
        """
        gatewayaddress = ipaddress.ip_address(gateway)
        # If gateway is reacheable add the route and return from method.
        for net in self.routes:
            if gatewayaddress in ipaddress.ip_network(net).hosts():
                self.routes[destination] = gateway
                return
        # Raise the exception if gateway is not reacheable.
        raise ValueError("Gateway is unreacheable.")

    def delete_route(self, network):
        """Deletes route to network from routes dictionary.
        Args:
            network: network in CIDR notation to delete from route table
        """
        if network in self.routes:
            self.routes.pop(network)
    
    def show_routes(self):
        """Prints route table"""
        for network in self.routes:
            print(f"{network} - {self.routes[network]}")



router = Router()
router.add_address('192.168.5.14/24', 'eth1')
print("Interfaces:")
router.show_addresses()
print('Route table:')
router.show_routes()
print('Add some routes:')
router.add_route('172.16.0.0/16', '192.168.5.1')
router.add_route('172.24.0.0/16', '172.16.8.1')
print('Route table:')
router.show_routes()
print('Delete interface')
router.delete_address('192.168.5.14/24')
print('Route table:')
router.add_route('172.24.0.0/16', '192.168.8.1')