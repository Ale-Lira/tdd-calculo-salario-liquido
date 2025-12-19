import unittest
from salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):
    
    # Definição das constantes usadas nos testes (Baseado no seu Enunciado)
    TETO_INSS = 900.00 # Valor assumido para o exercício
    LIMITE_ISENCAO_IR = 2000.00
    ALIQUOTA_INSS = 0.08
    ALIQUOTA_IR = 0.10

    def setUp(self):
        """Prepara o ambiente antes de cada teste"""
        self.calculator = SalaryCalculator()

    # --- Testes de CORREÇÃO FUNCIONAL (Regras de Negócio) ---

    def test_salario_bruto_isento_ir(self):
        """
        Cenário: Salário R$ 1.500,00 (Abaixo de 2000)
        INSS: 1500 * 0.08 = 120.00 (Não atinge teto)
        IR: Isento (0.00)
        Liquido Esperado: 1500 - 120 - 0 = 1380.00
        """
        resultado = self.calculator.calculate_net_salary(1500.00)
        self.assertEqual(resultado, 1380.00)

    def test_salario_bruto_com_ir_sem_teto_inss(self):
        """
        Cenário: Salário R$ 3.000,00 (Acima de 2000)
        INSS: 3000 * 0.08 = 240.00 (Não atinge teto de 900)
        IR: 3000 * 0.10 = 300.00 (10% sobre o total)
        Liquido Esperado: 3000 - 240 - 300 = 2460.00
        """
        resultado = self.calculator.calculate_net_salary(3000.00)
        self.assertEqual(resultado, 2460.00)

    def test_salario_bruto_com_teto_inss(self):
        """
        Cenário: Salário R$ 15.000,00 (Salário alto)
        INSS: 15000 * 0.08 = 1200.00 -> Limitado ao Teto de 900.00
        IR: 15000 * 0.10 = 1500.00
        Liquido Esperado: 15000 - 900 - 1500 = 12600.00
        """
        resultado = self.calculator.calculate_net_salary(15000.00)
        self.assertEqual(resultado, 12600.00)

    def test_arredondamento_duas_casas(self):
        """
        Cenário: Testar arredondamento matemático
        Salário: R$ 1.000,55
        INSS: 1000.55 * 0.08 = 80.044 -> Arredonda para 80.04
        IR: Isento
        Liquido: 1000.55 - 80.04 = 920.51
        """
        resultado = self.calculator.calculate_net_salary(1000.55)
        self.assertEqual(resultado, 920.51)

    # --- Testes de CONFIABILIDADE/ROBUSTEZ (Exceções) ---

    def test_salario_zero_deve_gerar_erro(self):
        """Regra: Salários iguais a zero devem gerar erro"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(0)

    def test_salario_negativo_deve_gerar_erro(self):
        """Regra: Salários inferiores a zero devem gerar erro"""
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(-500.00)

if __name__ == '__main__':
    unittest.main()
