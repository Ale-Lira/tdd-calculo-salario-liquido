class SalaryCalculator:
    # Constantes de negócio
    INSS_ALIQUOTA = 0.08
    INSS_TETO = 500.00

    VT_ALIQUOTA = 0.06
    IR_DEDUCAO_POR_DEPENDENTE = 150.00

    IR_FAIXA_ISENCAO = 2000.00
    IR_FAIXA_MEDIA = 4000.00

    def calculate_net_salary(
        self,
        gross_salary: float,
        dependents: int = 0,
        uses_transport_voucher: bool = False
    ) -> float:
        self._validate_input(gross_salary, dependents)

        inss = self._calculate_inss(gross_salary)
        irrf = self._calculate_irrf(gross_salary, dependents)
        vt = self._calculate_vt(gross_salary, uses_transport_voucher)

        return round(gross_salary - inss - irrf - vt, 2)

    # ---------- Métodos privados ----------

    def _validate_input(self, salary: float, dependents: int):
        if salary <= 0:
            raise ValueError("O salário bruto deve ser positivo.")
        if dependents < 0:
            raise ValueError("O número de dependentes não pode ser negativo.")

    def _calculate_inss(self, salary: float) -> float:
        return min(salary * self.INSS_ALIQUOTA, self.INSS_TETO)

    def _calculate_irrf(self, salary: float, dependents: int) -> float:
        if salary <= self.IR_FAIXA_ISENCAO:
            ir_base = 0.0
        elif salary <= self.IR_FAIXA_MEDIA:
            ir_base = salary * 0.10
        else:
            ir_base = salary * 0.20

        desconto_dependentes = dependents * self.IR_DEDUCAO_POR_DEPENDENTE
        return max(ir_base - desconto_dependentes, 0.0)

    def _calculate_vt(self, salary: float, uses_voucher: bool) -> float:
        return salary * self.VT_ALIQUOTA if uses_voucher else 0.0
