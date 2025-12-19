class SalaryCalculator:
    # Constantes atualizadas conforme novas regras
    INSS_ALIQUOTA = 0.08
    INSS_TETO = 500.00  # Atualizado de 900 para 500
    
    # Novas constantes para Manutenibilidade
    VT_ALIQUOTA = 0.06
    IR_DEDUCAO_POR_DEPENDENTE = 150.00
    
    # Limites das faixas de IR
    IR_FAIXA_ISENCAO = 2000.00
    IR_FAIXA_MEDIA = 4000.00
    
    def calculate_net_salary(self, gross_salary: float, dependents: int = 0, uses_transport_voucher: bool = False) -> float:
        # 1. Validação (Garante Confiabilidade e Robustez)
        self._validate_input(gross_salary, dependents)

        # 2. Cálculos isolados (Garante Testabilidade e Baixa Complexidade)
        inss = self._calculate_inss(gross_salary)
        irrf = self._calculate_irrf(gross_salary, dependents)
        vt = self._calculate_vt(gross_salary, uses_transport_voucher)

        # 3. Consolidação
        return self._calculate_final_value(gross_salary, inss, irrf, vt)

    def _validate_input(self, salary: float, dependents: int):
        if salary <= 0:
            raise ValueError("O salário bruto deve ser positivo.")
        if dependents < 0:
            raise ValueError("O número de dependentes não pode ser negativo.")

    def _calculate_inss(self, salary: float) -> float:
        calculated_inss = salary * self.INSS_ALIQUOTA
        return min(calculated_inss, self.INSS_TETO)

    def _calculate_irrf(self, salary: float, dependents: int) -> float:
        # Definição da base do imposto (Regra progressiva simples conforme enunciado)
        imposto_bruto = 0.0
        
        if salary <= self.IR_FAIXA_ISENCAO:
            imposto_bruto = 0.0
        elif salary <= self.IR_FAIXA_MEDIA:
            imposto_bruto = salary * 0.10
        else:
            imposto_bruto = salary * 0.20 # Nova alíquota para acima de 4000

        # Aplicação da dedução por dependentes
        total_deducao = dependents * self.IR_DEDUCAO_POR_DEPENDENTE
        
        # O imposto não pode ser negativo (max(0, valor))
        return max(imposto_bruto - total_deducao, 0.0)

    def _calculate_vt(self, salary: float, uses_voucher: bool) -> float:
        if uses_voucher:
            return salary * self.VT_ALIQUOTA
        return 0.0

    def _calculate_final_value(self, gross, inss, irrf, vt) -> float:
        return round(gross - inss - irrf - vt, 2)
