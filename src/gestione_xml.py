import os
import xml.etree.ElementTree as ET

def elenca_file_nella_cartella(cartella):
    """
    Elenca tutti i file presenti nella cartella specificata.

    Args:
        cartella (str): Il percorso della cartella.

    Returns:
        list: Una lista di nomi di file presenti nella cartella.
    """
    return [f for f in os.listdir(cartella) if os.path.isfile(os.path.join(cartella, f))]


def seleziona_file(file_list):
    """
    Permette all'utente di selezionare un file dall'elenco.

    Args:
        file_list (list): La lista dei file disponibili.

    Returns:
        str: Il nome del file selezionato.
    """
    for i, file_name in enumerate(file_list):
        print(f"{i + 1}. {file_name}")
    
    while True:
        try:
            scelta = int(input("Seleziona il numero del file da caricare: ")) - 1
            if 0 <= scelta < len(file_list):
                return file_list[scelta]
            else:
                print("Numero non valido. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

### @TO DELETE            
# def carica_file_selezionato(cartella, file_name):
#     """
#     Carica il file XML selezionato.

#     Args:
#         cartella (str): Il percorso della cartella.
#         file_name (str): Il nome del file da caricare.

#     Returns:
#         ElementTree: L'albero XML del file caricato.
#     """
#     file_path = os.path.join(cartella, file_name)
#     return ET.parse(file_path)
          
def leggi_config_xml(file_path):
    """
    Legge il file config.xml e restituisce una lista di "rung" con i suoi attributi.

    Args:
        file_path (str): Il percorso del file config.xml.

    Returns:
        list: Una lista di dizionari, ciascuno contenente gli attributi di un "rung".
    """
    # Analizza il file XML
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    rungs = []
    # Itera su ogni elemento "rung" nel file XML
    for rung in root.findall('rung'):
        # Estrae i valori degli attributi del "rung"
        comment = rung.find('comment').text if rung.find('comment').text is not None else ""
        prefisso = rung.find('Prefisso').text if rung.find('Prefisso').text is not None else ""
        ripetizione = rung.find('Ripetizione').text if rung.find('Ripetizione').text is not None else ""
        ripetizione_tipo = rung.find('Ripetizione').get('tipo') if rung.find('Ripetizione').text is not None else ""
        suffisso = rung.find('Suffisso').text if rung.find('Suffisso').text is not None else ""
        
        # Aggiunge gli attributi del "rung" alla lista
        rungs.append({
            'comment': comment,
            'prefisso': prefisso,
            'ripetizione': ripetizione,
            'ripetizione_tipo': ripetizione_tipo,
            'suffisso': suffisso
        })
    
    return rungs