import dbf
import os
import locale
from time import time

locale.setlocale(locale.LC_ALL, '')

class Finance():
    def __init__(self, window, path=None):
        self.path = path
        if path == None:
            self.path = '/home/andmor/emprueba/'
        self.window = window
        self.root = self.window.AddRoot('ROOT', 0)
        self.contabilidad = dbf.Table(os.path.join(self.path, 'contabilidad/CTW10005.DBF'))
        self.catalogo = dbf.Table(os.path.join(self.path, 'contabilidad/CTW10001.DBF'))
        self.catalogo.open()
        self.contabilidad.open()
        
        cur = time()
        self.contabilidad = self.contabilidad.create_index(lambda rec: rec.cuenta)
        print time() - cur


    def load_financials(self):
        
        n_i = self.catalogo.create_index(lambda rec: rec.cuenta)
        
        for i, record in enumerate(self.contabilidad):
            if '_' not in record['cuenta'] and record['tipo'] == 1 and record['eje'] == 2000:
                cargos = self.contabilidad[i + 1]['imp12']
                abonos = self.contabilidad[i + 2]['imp12']
                cargo_pa = record['imp11']

                saldo = cargos - abonos + cargo_pa
                
                if saldo != 0:
                    cu_cta = self.window.AppendItem(self.root, record['cuenta'], 0)

                    try:
                        self.window.SetItemText(cu_cta, n_i.search(match=(record['cuenta'],) , partial=False)[0]['nombre'], 1)
                        self.window.SetItemText(cu_cta, " "*(20-len(locale.currency(cargo_pa))) + locale.currency(cargo_pa, grouping=True), 2)
                        self.window.SetItemText(cu_cta, " "*(20-len(locale.currency(cargos))) + locale.currency(cargos, grouping=True), 3)
                        self.window.SetItemText(cu_cta, " "*(20-len(locale.currency(abonos))) + locale.currency(abonos, grouping=True), 4)
                        self.window.SetItemText(cu_cta, " "*(20-len(locale.currency(saldo))) + locale.currency(saldo, grouping=True), 5)
                    except UnicodeDecodeError:
                        pass

    #def sumaria(self, start, end):
        