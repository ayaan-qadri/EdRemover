import os

class c:
    h = '\033[95m'
    b = '\033[94m'
    k = '\033[96m'
    g = '\033[92m'
    w = '\033[93m'
    f = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    ul = '\033[4m'
    lr ='\033[91m'
banner = c.lr+f"""
 _____ ____  ____                                    
| ____|  _ \|  _ \ ___ _ __ ___   _____   _____ _ __ 
|  _| | | | | |_) / _ \ '_ ` _ \ / _ \ \ / / _ \ '__|
| |___| |_| |  _ <  __/ | | | | | (_) \ V /  __/ |   
|_____|____/|_| \_\___|_| |_| |_|\___/ \_/ \___|_| {c.k} 
                \n\t\t  Made By Krunal      
    """+c.end
print(banner)
choice = input("where do you want to clean empty folder:\n-> From everywhere - E\n-> From perticular folder - P: ").lower()
def cleaner1():
    def remove_empty_folders(path_abs):
        walk = list(os.walk(path_abs))
        for path, _, _ in walk[::-1]:
            if len(os.listdir(path)) == 0:
                os.rmdir(path)
                

    if __name__ == '__main__':
        remove_empty_folders("your-path")
    print("\n<<<<<- Empty folder removed  >>>>>")

def cleaner2():
    directory = input("-> Type folder name(case_sensitive): ").strip()
    
    parent = "D:/Hacktoberfest/EdRemover"
    
    path = os.path.join(parent, directory)
    
    try:
        os.rmdir(path)
        print("Directory '% s' has been removed successfully" % directory)
    except OSError as error:
        print(error)
        print("Directory '% s' can not be removed" % directory)

if choice == "e":
    cleaner1()
else:
    cleaner2()