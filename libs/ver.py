from colorama import Fore, init

version = "0.5"

init(autoreset=True)

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN
black = Fore.BLACK

msg = (cyan + "[" + green + "NOVUS" + cyan + "] " + cyan + "Novus Server Running on Version " + yellow + version)

def tellVersion():
    print(msg)