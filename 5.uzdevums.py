def ierakstit_vardu_faila(vards):
    try:
        with open('piektaisuzd.txt', 'a', encoding='utf-8') as f:
            f.write(vards + '\n')
        print(f"Vārds '{vards}' veiksmīgi ierakstīts failā 'piektaisuzd.txt'.")
    except IOError:
        print("Rakstīšanas kļūda: Failam nav pieejams rakstīšanas atļaujas vai tas ir aizņemts.")
    except Exception as e:
        print(f"Kļūda: {e}")

lietotaja_vards = input("Ievadiet savu vārdu: ")

ierakstit_vardu_faila(lietotaja_vards)