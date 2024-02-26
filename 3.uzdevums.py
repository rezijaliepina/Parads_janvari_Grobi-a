def lasit_datni():
    try:
        with open('3uzd.txt', 'r', encoding='utf-8') as f:
            rindas = f.readlines()
            if len(rindas) >= 3:
                tresa_rinda = rindas[2]
                print(tresa_rinda)
            else:
                print("Failā ir mazāk par trim rindām.")
        
    except FileNotFoundError:
        print("Kļūda:datni nevar atrast!")

if __name__=="__main__":
    lasit_datni()