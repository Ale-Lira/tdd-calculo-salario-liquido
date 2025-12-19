import unittest
from salary_calculator import SalaryCalculator


class TestSalaryCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SalaryCalculator()

    # --- INSS ---

    def test_inss_abaixo_teto(self):
        result = self.calculator.calculate_net_salary(3000.00)
        self.assertEqual(result, 2460.00)

    def test_inss_com_teto_maximo(self):
        result = self.calculator.calculate_net_salary(10000.00)
        self.assertEqual(result, 7500.00)

    # --- IR Progressivo ---

    def test_ir_isento_ate_2000(self):
        result = self.calculator.calculate_net_salary(2000.00)
        self.assertEqual(result, 1840.00)

    def test_ir_10_porcento(self):
        result = self.calculator.calculate_net_salary(3000.00)
        self.assertEqual(result, 2460.00)

    def test_ir_20_porcento(self):
        result = self.calculator.calculate_net_salary(5000.00)
        self.assertEqual(result, 3600.00)

    # --- Dependentes ---

    def test_deducao_por_dependente(self):
        result = self.calculator.calculate_net_salary(3000.00, dependents=1)
        self.assertEqual(result, 2610.00)

    def test_ir_nao_pode_ser_negativo(self):
        result = self.calculator.calculate_net_salary(3000.00, dependents=3)
        self.assertEqual(result, 2760.00)

    # --- Vale Transporte ---

    def test_desconto_vale_transporte(self):
        result = self.calculator.calculate_net_salary(
            2000.00,
            uses_transport_voucher=True
        )
        self.assertEqual(result, 1720.00)

    # --- Validações ---

    def test_salario_negativo_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(-100.00)

    def test_dependentes_negativos_deve_gerar_erro(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(3000.00, dependents=-1)


if __name__ == "__main__":
    unittest.main()
