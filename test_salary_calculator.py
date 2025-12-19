import unittest
from salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = SalaryCalculator()
        print("\n" + "="*60)

    # --- Testes de INSS (Regra Atualizada: Teto R$ 500,00) ---

    def test_inss_abaixo_teto(self):
        print("TESTE: INSS Abaixo do Teto e IR 10%")
        gross = 3000.00
        expected = 2460.00
        
        result = self.calculator.calculate_net_salary(gross)
        
        print(f"Entrada: Salário R$ {gross:.2f}")
        print(f"Cálculo: 3000 - 240(INSS) - 300(IR)")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    def test_inss_novo_teto_500(self):
        print("TESTE: INSS no Novo Teto (R$ 500) e IR 20%")
        gross = 10000.00
        expected = 7500.00
        
        result = self.calculator.calculate_net_salary(gross)
        
        print(f"Entrada: Salário R$ {gross:.2f}")
        print(f"Cálculo: 10000 - 500(Teto INSS) - 2000(IR 20%)")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    # --- Testes de IR Progressivo (Novas Faixas) ---

    def test_ir_faixa_20_porcento(self):
        print("TESTE: Faixa de IR de 20% (Salário > 4000)")
        gross = 5000.00
        expected = 3600.00
        
        result = self.calculator.calculate_net_salary(gross)
        
        print(f"Entrada: Salário R$ {gross:.2f}")
        print(f"Cálculo: 5000 - 400(INSS) - 1000(IR 20%)")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    # --- Testes de Vale Transporte (Nova Regra: 6%) ---

    def test_desconto_vale_transporte(self):
        print("TESTE: Desconto de Vale Transporte (6%)")
        gross = 2000.00
        uses_vt = True
        expected = 1720.00
        
        result = self.calculator.calculate_net_salary(gross, uses_transport_voucher=uses_vt)
        
        print(f"Entrada: Salário R$ {gross:.2f} | VT: Sim")
        print(f"Cálculo: 2000 - 160(INSS) - 0(IR) - 120(VT)")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    # --- Testes de Dependentes (Dedução de R$ 150 no IR) ---

    def test_deducao_dependente_no_ir(self):
        print("TESTE: Dedução de IR por Dependente")
        gross = 3000.00
        deps = 1
        expected = 2610.00
        
        result = self.calculator.calculate_net_salary(gross, dependents=deps)
        
        print(f"Entrada: Salário R$ {gross:.2f} | Deps: {deps}")
        print(f"IR Base: 300.00 | Dedução: 150.00 | IR Final: 150.00")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    def test_deducao_dependente_nao_negativa_ir(self):
        print("TESTE: Dedução de Dependente não gera imposto negativo")
        gross = 3000.00
        deps = 3
        expected = 2760.00
        
        result = self.calculator.calculate_net_salary(gross, dependents=deps)
        
        print(f"Entrada: Salário R$ {gross:.2f} | Deps: {deps}")
        print(f"IR Base: 300.00 | Dedução: 450.00 | IR Final: 0.00 (Isento)")
        print(f"Esperado: R$ {expected:.2f} | Obtido: R$ {result:.2f}")
        
        self.assertEqual(result, expected)

    # --- Testes de Confiabilidade (Exceções) ---

    def test_erro_dependentes_negativos(self):
        print("TESTE: Erro para Dependentes Negativos")
        print("Entrada: Deps = -1")
        try:
            self.calculator.calculate_net_salary(3000.00, dependents=-1)
        except ValueError as e:
            print(f"Exceção capturada com sucesso: '{e}'")
            self.assertTrue(True)
        else:
            self.fail("Deveria ter lançado ValueError")

    def test_erro_salario_negativo(self):
        print("TESTE: Erro para Salário Negativo")
        print("Entrada: Salário = -100")
        try:
            self.calculator.calculate_net_salary(-100.00)
        except ValueError as e:
            print(f"Exceção capturada com sucesso: '{e}'")
            self.assertTrue(True)
        else:
            self.fail("Deveria ter lançado ValueError")

if __name__ == '__main__':
    unittest.main()
