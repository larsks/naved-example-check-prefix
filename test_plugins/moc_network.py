import netaddr


def network_contains(cidr, addr):
    return addr in netaddr.IPNetwork(cidr)


class TestModule:
    def tests(self):
        return {
            "network_contains": network_contains,
        }
