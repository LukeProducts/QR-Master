from pyzbar.pyzbar import decode
from PIL import Image
import pyqrcode
import colorama
from colorama import Fore, Style
colorama.init()

opts = ["encoder", "decoder"]
ForeColor = ["green", "blue"]
ForeColor.sort()
BackColor = ["green", "blue"]
BackColor.sort()
def encode():
    Code = input("Input for Code content:\n>> ")
    File = input("Enter output file name:\n>> ")
    print(Fore.GREEN)
    print("Texture colors:" + Fore.LIGHTMAGENTA_EX)
    for i in ForeColor:
        print(i)
    ModuleColor = input(Fore.RESET + "Enter Texture color:\n>> ")
    if ModuleColor == ForeColor[0]:
        print(Fore.MAGENTA + "color >> " + Fore.LIGHTBLUE_EX + ForeColor[0] + Fore.RESET)
        module_color = (0, 0, 255)
    elif ModuleColor == ForeColor[1]:
        print(Fore.MAGENTA + "color >> " + Fore.LIGHTGREEN_EX + ForeColor[1] + Fore.RESET)
        module_color = (0, 255, 0)
    else:
        print(Fore.RED + Style.BRIGHT + "unknown color" + "\n" + Style.RESET_ALL + Fore.LIGHTGREEN_EX + "selecting Default:'black'" + Fore.RESET)
        module_color = (0, 0, 0, 255)
    print(Fore.GREEN)
    print("Texture colors:" + Fore.LIGHTMAGENTA_EX)
    for i in BackColor:
        print(i)
    BackgroundColor = input(Fore.RESET + "Enter Background color:\n>> ")
    if BackgroundColor == BackColor[0]:
        print(Fore.MAGENTA + "color >> " + Fore.LIGHTBLUE_EX + BackColor[0] + Fore.RESET)
        background = (0, 0, 255)
    elif BackgroundColor == BackColor[1]:
        print(Fore.MAGENTA + "color >> " + Fore.LIGHTGREEN_EX + BackColor[1] + Fore.RESET)
        background = (0, 255, 0)
    else:
        print(Fore.RED + Style.BRIGHT + "unknown color" + "\n" + Style.RESET_ALL + Fore.LIGHTGREEN_EX + "selecting Default:'white'" + Fore.RESET)
        background = (255, 255, 255, 255)


    fileformat = str(File) + ".png"
    QR = pyqrcode.create(str(Code))
    QR.png(fileformat, scale=8, module_color=module_color, background=background)
    print(Fore.LIGHTGREEN_EX + "Process finfished" + "\n" + Fore.BLUE +"output file: " + Fore.RED + fileformat + Fore.RESET)

def pic():
    print(Fore.CYAN)
    print("""
                                           
     QQQQQQQQQ     RRRRRRRRRRRRRRRRR   
   QQ:::::::::QQ   R::::::::::::::::R  
 QQ:::::::::::::QQ R::::::RRRRRR:::::R 
Q:::::::QQQ:::::::QRR:::::R     R:::::R
Q::::::O   Q::::::Q  R::::R     R:::::R
Q:::::O     Q:::::Q  R::::R     R:::::R
Q:::::O     Q:::::Q  R::::RRRRRR:::::R 
Q:::::O     Q:::::Q  R:::::::::::::RR  
Q:::::O     Q:::::Q  R::::RRRRRR:::::R 
Q:::::O     Q:::::Q  R::::R     R:::::R
Q:::::O  QQQQ:::::Q  R::::R     R:::::R
Q::::::O Q::::::::Q  R::::R     R:::::R
Q:::::::QQ::::::::QRR:::::R     R:::::R
 QQ::::::::::::::Q R::::::R     R:::::R
   QQ:::::::::::Q  R::::::R     R:::::R
     QQQQQQQQ::::QQRRRRRRRR     RRRRRRR
             Q:::::Q                   
              QQQQQQ                   
                                       
    
    """)
    print(Fore.MAGENTA)
    print(Style.BRIGHT)
    print("QR operating Options:")
    for option in opts:
        print("'" + option + "'")
    print(Style.NORMAL)
    print(Fore.RESET)

pic()
X = input(">>")
if X == 'encoder':
    encode()
elif X == 'decoder':
    File = input("Enter File Name:\n>> ")
    try:

        content = decode(Image.open(str(File)))

        if content == []:
            print(Fore.RED)
            print("Es wurde keine QR - Information gefunden")
            print(Fore.RESET)
        else:
            print(Fore.GREEN)
            print("Content found:")
            print("QR content:")
            print(content)
            print(Fore.RESET)

    except:
        print(Fore.YELLOW)
        print("File does not exist")
        print(Fore.RESET)

else:
    print(Fore.RED)
    print("unknown command")
    print(Fore.RESET)

