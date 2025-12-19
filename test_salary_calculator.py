import unittest
from salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = SalaryCalculator()

    # --- Testes de INSS (Regra Atualizada: Teto R$ 500,00) ---

    def test_inss_abaixo_teto(self):
        """
        Salário R$ 3.000,00
        INSS: 3000 * 0.08 = 240.00 (Menor que 500)
        IR (Faixa 10%): 3000 * 0.10 = 300.00
        Líquido: 3000 - 240 - 300 = 2460.00
        """
        # Nota: dependents=0 e uses_transport_voucher=False por padrão
        resultado = self.calculator.calculate_net_salary(3000.00) 
        self.assertEqual(resultado, 2460.00)

    def test_inss_novo_teto_500(self):
        """
        Salário R$ 10.000,00
        INSS: 10000 * 0.08 = 800.00 -> Teto é 500.00
        IR (Faixa 20%): 10000 * 0.20 = 2000.00
        Líquido: 10000 - 500 - 2000 = 7500.00
        """
        resultado = self.calculator.calculate_net_salary(10000.00)
        self.assertEqual(resultado, 7500.00)

    # --- Testes de IR Progressivo (Novas Faixas) ---

    def test_ir_faixa_20_porcento(self):
        """
        Salário R$ 5.000,00
        INSS: 5000 * 0.08 = 400.00
        IR (> 4000): 5000 * 0.20 = 1000.00
        Líquido: 5000 - 400 - 1000 = 3600.00
        """
        resultado = self.calculator.calculate_net_salary(5000.00)
        self.assertEqual(resultado, 3600.00)

    # --- Testes de Vale Transporte (Nova Regra: 6%) ---

    def test_desconto_vale_transporte(self):
        """
        Salário R$ 2.000,00 (Isento IR)
        INSS: 2000 * 0.08 = 160.00
        VT (True): 2000 * 0.06 = 120.00
        Líquido: 2000 - 160 - 0 - 120 = 1720.00
        """
        resultado = self.calculator.calculate_net_salary(
            gross_salary=2000.00, 
            dependents=0, 
            uses_transport_voucher=True
        )
        self.assertEqual(resultado, 1720.00)

    # --- Testes de Dependentes (Dedução de R$ 150 no IR) ---

    def test_deducao_dependente_no_ir(self):
        """
        Salário R$ 3.000,00
        INSS: 240.00
        IR Base (10%): 300.00
        Dedução (1 dep): -150.00
        IR Final: 150.00
        Líquido: 3000 - 240 - 150 = 2610.00
        """
        resultado = self.calculator.calculate_net_salary(
            gross_salary=3000.00, 
            dependents=1
        )
        self.assertEqual(resultado, 2610.00)

    def test_deducao_dependente_nao_negativa_ir(self):
        """
        Teste de Borda: Dedução maior que o imposto devido.
        Salário R$ 3.000,00
        IR Base (10%): 300.00
        Dedução (3 dep): 3 * 150 = 450.00
        IR Final: 300 - 450 = -150 -> Deve ser 0.00 (Não pode ser negativo)
        Líquido: 3000 - 240 - 0 = 2760.00
        """
        resultado = self.calculator.calculate_net_salary(
            gross_salary=3000.00, 
            dependents=3
        )
        self.assertEqual(resultado, 2760.00)

    # --- Testes de Confiabilidade (Exceções) ---

    def test_erro_dependentes_negativos(self):
        """Regra: Número de dependentes < 0 deve gerar erro"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(3000.00, dependents=-1)

    def test_erro_salario_negativo(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(-100.00)

if __name__ == '__main__':
    unittest.main()
