

def single_rung_creation(rung, module_names):
    """
    Crea una stringa concatenata con i campi di rung in questo ordine:
    prefisso, per ogni module_names concatena il suo valore con ripetizione,
    e infine concatena con suffisso. Tutti i campi sono separati da ";".

    Args:
        rung (dict): Dizionario contenente gli attributi del "rung".
        module_names (list): Lista di nomi di moduli da concatenare con ripetizione.

    Returns:
        str: Stringa concatenata con i campi di rung.
    """
    # Inizia con il prefisso
    result = rung['prefisso']
    
    # Concatena ogni module_name con ripetizione
    for module_name in module_names:
        str_ripetizione = rung['ripetizione'].replace("MODULO", module_name)
        result += f"{str_ripetizione}"
    
    # Concatena il suffisso
    result += f"{rung['suffisso']}"
    
    return result