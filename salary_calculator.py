class SalaryCalculator:
    # Constantes de Negócio (Melhora a Manutenibilidade)
    # Se a lei mudar, alteramos apenas aqui, sem mexer na lógica.
    INSS_ALIQUOTA = 0.08
    INSS_TETO = 900.00
    IR_LIMITE_ISENCAO = 2000.00
    IR_ALIQUOTA = 0.10

    def calculate_net_salary(self, gross_salary: float) -> float:
        """
        Método principal que orquestra o cálculo.
        Foca na legibilidade e no fluxo do processo.
        """
        self._validate_input(gross_salary)

        inss = self._calculate_inss(gross_salary)
        irrf = self._calculate_irrf(gross_salary)

        return self._calculate_final_value(gross_salary, inss, irrf)

    def _validate_input(self, salary: float):
        """Garante a Confiabilidade e Robustez"""
        if salary <= 0:
            raise ValueError("O salário bruto deve ser positivo.")

    def _calculate_inss(self, salary: float) -> float:
        """Encapsula a regra do INSS (Coesão)"""
        calculated_inss = salary * self.INSS_ALIQUOTA
        return min(calculated_inss, self.INSS_TETO)

    def _calculate_irrf(self, salary: float) -> float:
        """Encapsula a regra do IR (Coesão)"""
        if salary > self.IR_LIMITE_ISENCAO:
            return salary * self.IR_ALIQUOTA
        return 0.0

    def _calculate_final_value(self, gross, inss, irrf) -> float:
        """Centraliza a regra de subtração e arredondamento"""
        return round(gross - inss - irrf, 2)
