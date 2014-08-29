from checkServerHandler import CheckServerHandler
from loginHandler import LoginHandler

#1 = Check Server
def EventHandler(package, config):
    if package["Status"] == 1:
        return CheckServerHandler(package)
    if package["Status"] == 2:
        return LoginHandler(package, config)
    