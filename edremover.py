import os,time,threading
os.system("clear && clear")
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
                \n\t\t  Made By Ayaan      
    """+c.end
try:

    print(banner)
    where = input(c.k+f"where do you want to clean empty folder:\n{c.end}-> From everywhere - E\n-> From perticular folder - P: ").lower()
    remove = 0
    def cleaner():
        global remove
        for path,folder,file in os.walk("/storage/emulated/0"):
            for f in folder:
                full_path = os.path.join(path,f)
                try:
                    remove += 1
                    os.rmdir(full_path)
                except OSError:
                    remove -= 1
                finally:
                    for e in ["Removing empty folder..."]:
                        time.sleep(0.000001)
                        print(" "*24,end="\r")
                        time.sleep(0.0000001)
                        print(e,end="\r")
        print(f"\n<<<<<  {remove} - Empty folder removed  >>>>>")
    
    
    def cleaner2():
        where2 = input("-> Type folder name(case_sensitive): ").strip()
        if where2:
            main_path = "/storage/emulated/0"
            full_path = os.path.join(main_path,where2)
            if os.path.exists(full_path):
                for path,folder,file in os.walk(full_path):
                    for f in folder:
                        full_path = os.path.join(path,f)
                        try:
                            global remove
                            remove += 1
                            os.rmdir(full_path)
                        except OSError:
                            remove -= 1
                        finally:
                            for e in ["Removing empty folder..."]:
                                time.sleep(0.00001)
                                print("\n "*24,end="\r")
                                time.sleep(0.0000001)
                                print(e,end="\r")
            else:
                print("\n-> You entered folder name doesn't exists")
        else:
            print("\n   ___Empty input not allow___")
        print(f"\n<<<<<  {remove} - Empty folder removed  >>>>>")
            
    if where == "e":
        cleaner()
    else:
        cleaner2()
except KeyboardInterrupt:
    print("\n\t~~~~~  See you soon :)  ~~~~~")