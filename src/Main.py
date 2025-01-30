from gestione_xml import leggi_config_xml
import rung_generator as rg

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
    
    rung1 = rg.single_rung_creation(rungs[0], module_names)
    print(rung1)
    
if __name__ == "__main__":
    main()
