import unittest
import sys
import os

# Aggiungi il percorso della cartella 'src' al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rung_generator import single_rung_creation

class TestRungGenerator(unittest.TestCase):
    """
    Classe di test per la funzione single_rung_creation.
    """
    
    def test_single_rung_creation(self):
        """
        Testa la funzione single_rung_creation per verificare che la stringa concatenata
        sia corretta con i campi di rung nell'ordine specificato.
        """
        # Dati di input
        rung = {
            'comment': 'Questo è un commento',
            'prefisso': 'XIO(Loc_GLOBAL_Fault)',
            'ripetizione': '[XIC(MODULO.FBK.AlmOk) ,XIC(MODULO.FBK.Module_disabled) XIO(MODULO.FBK.ModeManual) ]',
            'ripetizione_tipo': 'serie',
            'suffisso': 'OTE(GLOBAL.FBK.MOD.AlmOk)'
        }
        module_names = ['PINF1', 'FILL', 'BOXT']
        
        # Risultato atteso
        expected_result = 'XIO(Loc_GLOBAL_Fault)[XIC(PINF1.FBK.AlmOk) ,XIC(PINF1.FBK.Module_disabled) XIO(PINF1.FBK.ModeManual) ][XIC(FILL.FBK.AlmOk) ,XIC(FILL.FBK.Module_disabled) XIO(FILL.FBK.ModeManual) ][XIC(BOXT.FBK.AlmOk) ,XIC(BOXT.FBK.Module_disabled) XIO(BOXT.FBK.ModeManual) ]OTE(GLOBAL.FBK.MOD.AlmOk)'
              
        # Chiamata alla funzione e verifica del risultato
        result = single_rung_creation(rung, module_names)
        #print(result)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()