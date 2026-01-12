import os
import sys
import time

# ألوان الشيطان
R = '\033[1;31m' # الأحمر للنظام
G = '\033[1;32m' # الأخضر للأوامر
Y = '\033[1;33m' # الأصفر للتحذير
W = '\033[0m'    # الأبيض للرسائل

def clear_screen():
    os.system('clear')

def show_logo():
    print(R + """
      .---.              .-----------.
     /     \    __      /    .---.    \ 
    / /     \  (  )    /    /     \    \ 
   //////    ' \/ `   //////      |
  //// [  PIRATE-S35 ] ////       |
 //////      (☠️ )    //////       /
      `----------'            /
     _______WIFI-DEVIL_______/
    """ + Y + """
   [☠️ ] Developer: Gathan (THE-DEVIL)
   [☠️ ] Power: WiFi Stealth Protocol
   -----------------------------------------
    """ + W)

def start_pirate():
    clear_screen()
    show_logo()
    print(G + "[1] " + W + "جلب بيانات الشبكة (IP/Gateway) واستخراج الرمز")
    print(G + "[2] " + W + "كشف الشبكات المخفية وفك رموزها")
    print(G + "[3] " + W + "إنشاء نقطة وهمية (Evil Twin) لاصطياد الضحايا")
    print(R + "[4] " + W + "خروج من مملكة الشيطان")
    
    cmd = input("\n" + R + "[PIRATE@S35]:# " + W)
    
    if cmd == '1':
        print(Y + "\n[*] جاري سحب بيانات الشبكة الحالية..." + W)
        os.system("ip route show | grep default")
        os.system("ifconfig wlan0 | grep inet")
        print(R + "[!] محاولة سحب الرمز (يتطلب صلاحية Root)..." + W)
        os.system("su -c 'cat /data/misc/wifi/wpa_supplicant.conf | grep psk'")
        input("\nاضغط Enter للعودة..."); start_pirate()
        
    elif cmd == '2':
        print(Y + "\n[*] جاري البحث عن الإشارات المخفية (Airodump-ng)..." + W)
        os.system("airodump-ng wlan0")
        input("\nاضغط Enter للعودة..."); start_pirate()
        
    elif cmd == '3':
        name = input(Y + "أدخل اسم الشبكة الوهمية: " + W)
        code = input(Y + "أدخل رمز الشبكة للصيد: " + W)
        print(R + f"\n[!] تم إطلاق {name}.. الشيطان بانتظار الضحايا..." + W)
        os.system(f"nmcli dev wifi hotspot ssid {name} password {code}")
        input("\nاضغط Enter لإغلاق الفخ..."); start_pirate()
        
    elif cmd == '4':
        print(R + "\nوداعاً.. القراصنة لا يتركون خلفهم أثراً." + W)
        sys.exit()
    else:
        start_pirate()

if __name__ == "__main__":
    start_pirate()
  
