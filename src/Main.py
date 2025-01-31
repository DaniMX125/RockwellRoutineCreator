from gestione_xml import leggi_config_xml
import rung_generator as rg
import gestione_l5x as gl

def main():
    print("Benvenuto nel generatore di routine rockwell!")
        
    module_number = input("Quanti moduli hai?: ").strip()
    module_names = []
    for i in range(int(module_number)):
        module_names.append(input(f"Nome del modulo {i+1}: ").strip())
        #print(f"Modulo {i+1}")
        
    # Esempio di utilizzo
    file_path = 'c:/Users/Administrator/Documents/Progetti/Python/RockwellRoutineCreator/src/config.xml'
    rungs = leggi_config_xml(file_path)
    # for rung in rungs:
    #     print(rung)
    
    with open("output.l5x", "w", encoding="utf-8") as f:
        f.write(gl.routine_l5x_inizio())
        for i, rung in enumerate(rungs):
            rung_string = rg.single_rung_creation(rung, module_names)
            f.write(gl.routine_l5x_rung(i, rung['comment'], rung_string))
        f.write(gl.routine_l5x_fine())
    
    f.close()
         
    #rung_string = rg.single_rung_creation(rungs[0], module_names)
    
    #print(gl.routine_l5x_rung(1, "Commento", "Testo"))
    return
    #print(rung_string)
    
if __name__ == "__main__":
    main()
