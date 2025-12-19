class SalaryCalculator:
    # Mantendo constantes antigas por enquanto (serão alteradas no Refactor)
    INSS_ALIQUOTA = 0.08
    INSS_TETO = 900.00  # O teste vai falhar pois agora esperamos 500
    IR_LIMITE_ISENCAO = 2000.00
    IR_ALIQUOTA = 0.10

    # Atualizei a assinatura para aceitar os novos parâmetros com valores padrão (Backward Compatibility)
    def calculate_net_salary(self, gross_salary: float, dependents: int = 0, uses_transport_voucher: bool = False) -> float:
        self._validate_input(gross_salary)
        
        # A lógica abaixo AINDA É A ANTIGA. Os testes VÃO FALHAR.
        inss = self._calculate_inss(gross_salary)
        irrf = self._calculate_irrf(gross_salary)
        
        return self._calculate_final_value(gross_salary, inss, irrf)

    def _validate_input(self, salary: float):
        if salary <= 0:
            raise ValueError("O salário bruto deve ser positivo.")

    def _calculate_inss(self, salary: float) -> float:
        calculated_inss = salary * self.INSS_ALIQUOTA
        return min(calculated_inss, self.INSS_TETO)

    def _calculate_irrf(self, salary: float) -> float:
        if salary > self.IR_LIMITE_ISENCAO:
            return salary * self.IR_ALIQUOTA
        return 0.0

    def _calculate_final_value(self, gross, inss, irrf) -> float:
        return round(gross - inss - irrf, 2)
