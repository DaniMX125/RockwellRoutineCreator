import xml.etree.ElementTree as ET

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
        comment = rung.find('comment').text
        prefisso = rung.find('Prefisso').text
        ripetizione = rung.find('Ripetizione').text
        ripetizione_tipo = rung.find('Ripetizione').get('tipo')
        suffisso = rung.find('Suffisso').text
        
        # Aggiunge gli attributi del "rung" alla lista
        rungs.append({
            'comment': comment,
            'prefisso': prefisso,
            'ripetizione': ripetizione,
            'ripetizione_tipo': ripetizione_tipo,
            'suffisso': suffisso
        })
    
    return rungs