
def routine_l5x_inizio():
    '''
    Questa funzione ritorna l'inizio della routine l5x
    '''
    string_inizio = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<RSLogix5000Content SchemaRevision="1.0" SoftwareRevision="35.00" TargetName="MainRoutine" TargetType="Routine" TargetSubType="RLL" ContainsContext="true" Owner="x" ExportDate="Fri Jan 31 09:25:02 2025" ExportOptions="References NoRawData L5KData DecoratedData Context Dependencies ForceProtectedEncoding AllProjDocTrans">
<Controller Use="Context">
<Programs Use="Context">
<Program Use="Context">
<Routines Use="Context">
<Routine Use="Target" Name="GeneratedRoutine" Type="RLL">
<RLLContent>\n'''
    return string_inizio   


def routine_l5x_fine():
    '''
    Questa funzione ritorna la fine della routine l5x
    '''
    string_fine = f'''</RLLContent>
</Routine>
</Routines>
</Program>
</Programs>
</Controller>
</RSLogix5000Content>
'''
    return string_fine

def routine_l5x_rung(rung_number, rung_comment, rung_text):
    '''
    Questa funzione ritorna una rung l5x
    '''
    string_result = f'''<Rung Number="{rung_number}" Type="N">\n'''
    string_comment = f'''<Comment>\n<![CDATA[{rung_comment}]]>\n</Comment>\n'''
    string_text = f'''<Text>\n<![CDATA[{rung_text};]]>\n</Text>\n'''
    string_result += string_comment + string_text + '''</Rung>\n'''

    return string_result