from parsl.addresses import address_by_route, address_by_hostname
import getpass

global_options = {
    'username': getpass.getuser(),
    'email': 'USER@USERDOMAIN.COM',
    'broker_address': '127.0.0.1',
    'broker_port': 8088,
    'endpoint_address': address_by_hostname(),
}
