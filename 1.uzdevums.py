def lasit_datni():
    try:
        with open('1uzd.txt','r',encoding='utf8') as fails:
            datnes_saturs=fails.read()
            print(datnes_saturs)
        
        
    except FileNotFoundError:
        print("Kļūda:datni nevar atrast!")

if __name__=="__main__":
    lasit_datni()