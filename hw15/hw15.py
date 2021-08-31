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
        print(f"Interface {interface} was added with address {address}.\nDirectly connected network {connectednetwork} was added to route table.")
        
    def delete_address(self, address):
        """ Deletes address from addresses dictionary.
        Deletes routes to networks.
        Args:
            address: string containing IP address in CIDR notation
        Prints:
            string: "Address was deleted." if interface was deleted
            string: "There is no address assigned to any interface." if there is no interface with address
        Return:
            True if interface was deleted
            False if there is no interface with this address
        """
        if address in self.addresses:
            self.addresses.pop(address)
            print(f"Address {address} was deleted.")
            # The routes through the deleted gateway are not accessible now.
            connectednetwork = ipaddress.ip_interface(address).network
            # Add directly connected network to route table
            self.routes.pop(str(connectednetwork))
            print(f"Directly connected network {connectednetwork} was deleted from route table.")
            # We need to delete routes accessible through gateways in deleted network.
            self.update_route_table()
            return True
        print(f"There is no {address} assigned to any interface.")
        return False

    def show_addresses(self):
        """Shows interfaces with addresses"""
        print("Interfaces:")
        for address in self.addresses:
            print(f'{address} - {self.addresses[address]}')

    def add_route(self, destination, gateway):
        """Adds route to network
        Args: 
            destination: destination network address in CIDR notation
            gateway: address of gateway
        Returns:
            True if successfull
            False if destination is already in route table
        Raises:
            ValueError: gateway is unreachable
        """
        gatewayaddress = ipaddress.ip_address(gateway)
        # If desttination network is already in route table print it and return from method
        for net in self.routes:
            if net == destination:
                print(f"Route to {destination} already exists.")
                return False
        # If gateway is reacheable add the route and return from method.
        for net in self.routes:
            if gatewayaddress in ipaddress.ip_network(net).hosts():
                self.routes[destination] = gateway
                print(f"Route to {destination} was added with gateway {gateway}.")
                return True
        # Raise the exception if gateway is not reacheable.
        raise ValueError("Gateway is unreacheable.")
        

    def delete_route(self, network):
        """Deletes route to network from routes dictionary.
        Args:
            network: network in CIDR notation to delete from route table
        Returns:
            True if successfull
            False if there is no route to network in route table
        """
        if network in self.routes:
            self.routes.pop(network)
            print(f"Route to {network} was deleted from route table.")
            # We need to delete routes accessible through gateways in deleted network.
            self.update_route_table()
            return True
        print(f"There is no route to {network} in route table.")
        return False
    
    def show_routes(self):
        """Prints route table"""
        print("Route table:")
        for network in self.routes:
            print(f"{network} - {self.routes[network]}")

    def update_route_table(self):
        """Updates route table after deletion of interface or route table entry."""
        old_route_table = self.routes.copy()
        self.routes = {}
        for address in self.addresses:
            connectednetwork = ipaddress.ip_interface(address).network
            # Add directly connected network to route table
            self.routes[str(connectednetwork)] = address.split('/')[0]
        # Iteration over dictionary is unpredictable so we need to iterate over and over
        # while the resulting route table is stable.
        while True:
            # Counter of added to route table entries.
            counter = 0
            for route in old_route_table:
                try:
                    if self.add_route(route, old_route_table[route]):
                        counter += 1
                except ValueError:
                    pass
            # Break if all routes are in new route table.
            if counter == 0:
                break

        



router = Router()
router.add_address('192.168.5.14/24', 'eth1')
router.add_address('10.10.10.0/24', 'eth2')
router.show_addresses()
router.show_routes()
print('Add some routes:')
router.add_route('172.16.0.0/16', '192.168.5.1')

try:
    # Next line should raise an exception because the gateway is unreacheable
    router.add_route('172.24.0.0/16', '192.168.8.1')
except ValueError as err:
    print("An exception was catched.", err.args)

router.add_route('172.24.0.0/16', '172.16.8.1')
router.add_route('10.24.0.0/16', '10.10.10.12')
router.show_routes()
print('Delete interface')
router.delete_address('192.168.5.14/24')
router.show_addresses()
# Now the route table should be empty.
router.show_routes()
# Next line should raise an exception because the gateway is unreacheable
#print(router.add_route('172.24.0.0/16', '192.168.8.1'))