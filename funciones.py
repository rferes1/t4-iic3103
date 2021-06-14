## funciones

def elimina_ultimos_5_digitos(string):
    largo = len(string)
    largo5 = largo - 5
    string2 = string[:largo5]
    return string2

def eliminar_decimales(string):
    if string != None or type(string) == str:
        idx_punto = string.find(".")
        string2 = string[:idx_punto]
        return string2

def de_rate_a_popuilation(string, pais):
    p_chile = 17000000/100000
    p_ZAF = 50000000/100000
    p_NZL = 4000000/100000
    p_SWE = 10000000/100000
    p_ESP = 40000000/100000
    p_NDL = 15000000/100000
    lista_rate = [p_chile, p_NZL, p_ESP, p_ZAF, p_SWE, p_NDL]
    lista_paises = ['Chile', 'New Zealand', 'Spain', 'South Africa', 'Sweden', 'Netherlands']
    if string != None or type(string) == str:
        idx = lista_paises.index(pais)
        rate = lista_rate[idx]
        valor = eliminar_decimales(string)
        total = int(valor)*rate
        return str(total)


