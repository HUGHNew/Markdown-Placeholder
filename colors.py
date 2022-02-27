ENDC = "\033[0m"
def Header(content:str):
    return f"\033[95m{content}{ENDC}"
def Okblue(content:str):
    return f"\033[94m{content}{ENDC}"
def Okcyan(content:str):
    return f"\033[96m{content}{ENDC}"
def Okgreen(content:str):
    return f"\033[92m{content}{ENDC}"
def Warning(content:str):
    return f"\033[93m{content}{ENDC}"
def Fail(content:str):
    return f"\033[91m{content}{ENDC}"
def Bold(content:str):
    return f"\033[1m{content}{ENDC}"
def Underline(content:str):
    return f"\033[4m{content}{ENDC}"