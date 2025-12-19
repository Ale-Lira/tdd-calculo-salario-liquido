class SalaryCalculator:
    def calculate_net_salary(self, gross_salary):
        # 1. Validação de Confiabilidade/Robustez
        # Garante que o sistema rejeite valores inválidos conforme o teste
        if gross_salary <= 0:
            raise ValueError("O salário bruto deve ser positivo.")

        # 2. Cálculo do INSS (8% com Teto de 900.00)
        inss = gross_salary * 0.08
        if inss > 900.00:
            inss = 900.00

        # 3. Cálculo do IRRF (Isento até 2000, 10% do total acima disso)
        if gross_salary > 2000.00:
            irrf = gross_salary * 0.10
        else:
            irrf = 0.0

        # 4. Cálculo Líquido
        net_salary = gross_salary - inss - irrf

        # 5. Arredondamento (Regra de 2 casas decimais)
        return round(net_salary, 2)
