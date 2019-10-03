from pip._vendor.colorama import init, Fore

def display(message,is_writing=False):
    if is_writing:
        print(Fore.RED+'This is waening')
        print(Fore.WHITE + message)
    else:
        print(Fore.BLUE + message)