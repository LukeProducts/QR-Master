from pyzbar.pyzbar import decode
from PIL import Image
import pyqrcode
import colorama
from colorama import Fore, Back, Style
colorama.init()

opts = ["encoder", "decoder"]

def encode():
    Code = input("Input for Code content:\n>>")
    File = input("Enter output file name:\n>>")
    fileformat = str(File) + ".png"
    QR = pyqrcode.create(str(Code))
    QR.png(str(fileformat), scale=8)

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
    File = input("Enter File Name:\n>>")
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

