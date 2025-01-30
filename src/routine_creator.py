from gestione_xml import leggi_config_xml
    

def main():
    print("Benvenuto nel generatore di routine rockwell!")
    
    
    
    # Esempio di utilizzo
    file_path = 'c:/Users/Administrator/Documents/Progetti/Python/RockwellRoutineCreator/src/config.xml'
    rungs = leggi_config_xml(file_path)
    # for rung in rungs:
    #     print(rung)
    
    
if __name__ == "__main__":
    main()
