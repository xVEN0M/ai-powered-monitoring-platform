from scapy.all import ARP, Ether, srp


def scan_network(network_range: str):
    """
    Scan a network using ARP and return active hosts.
    """

    arp = ARP(pdst=network_range)
    ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ethernet / arp

    result = srp(
        packet,
        timeout=2,
        verbose=False
    )[0]

    devices = []

    for _, received in result:
        devices.append(
            {
                "ip": received.psrc,
                "mac": received.hwsrc
            }
        )

    return devices