import os
import sys
import gestione_xml as gx
import rung_generator as rg
import gestione_l5x as gl

def main():
    print("Benvenuto nel generatore di routine rockwell!")
        
    module_number = input("Quanti moduli hai?: ").strip()
    module_names = []
    for i in range(int(module_number)):
        module_names.append(input(f"Nome del modulo {i+1}: ").strip())
        #print(f"Modulo {i+1}")
     
    # Cartella dei file XML
    # Ottieni il percorso della directory corrente
    
    # Ottieni il percorso della directory dell'eseguibile
    if getattr(sys, 'frozen', False):
        # Se il programma è stato congelato con PyInstaller
        current_dir = os.path.dirname(sys.executable)
    else:
        # Se il programma è in esecuzione come script Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
    #print(f"Directory corrente: {current_dir}")
    
    # Costruisci il percorso relativo alla cartella ConfigFiles e OutputFiles
    config_dir = os.path.join(current_dir, 'ConfigFiles\\')
    output_dir = os.path.join(current_dir, 'OutputFiles\\')
    # Elenca i file nella cartella ConfigFiles
    file_list = gx.elenca_file_nella_cartella(config_dir)
    # Permetti all'utente di selezionare un file
    file_selezionato = gx.seleziona_file(file_list)
    file_output = file_selezionato.replace(".xml", ".l5x").replace("Config", "Output")  
          
    # Leggi il contenuto del file XML
    rungs = gx.leggi_config_xml(os.path.join(config_dir, file_selezionato))
    
    # Esempio di utilizzo
    #file_path = 'c:/Users/Administrator/Documents/Progetti/Python/RockwellRoutineCreator/src/config.xml'
    #rungs = leggi_config_xml(file_path)
    # for rung in rungs:
    #     print(rung)
    
    # Creazione del file l5x
    file_output = os.path.join(output_dir, file_output)
    with open(file_output, "w", encoding="utf-8") as f:
        f.write(gl.routine_l5x_inizio())
        for i, rung in enumerate(rungs):
            rung_string = rg.single_rung_creation(rung, module_names)
            f.write(gl.routine_l5x_rung(i, rung['comment'], rung_string))
        f.write(gl.routine_l5x_fine())
    
    f.close()
         
    #rung_string = rg.single_rung_creation(rungs[0], module_names)
    
    #print(gl.routine_l5x_rung(1, "Commento", "Testo"))
    print(f"File creato: {file_output}")
    input("Premi un tasto per uscire...")
    return
    #print(rung_string)
    
if __name__ == "__main__":
    main()
