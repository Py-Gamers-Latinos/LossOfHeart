from servidor import servidor
from setup import Setup

if __name__ == '__main__':
    Setup = Setup()
    host = Setup.host
    port = Setup.port
    del Setup
    print "Se ejecutara el servidor en: %s:%s" % (host, port)
    servidor(host, port)