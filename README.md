# 🧪 Estudo de TDD com Suporte de IA

Esse repositório é para o estudo da aplicação do ciclo de Desenvolvimento Orientado a Testes (TDD) com apoio de ferramentas de Inteligência Artificial, analisando seus impactos sobre a qualidade do software, design do código e métricas de software, no contexto da engenharia de software moderna.

O projeto consiste na implementação de uma calculadora de salário líquido, focando na lógica de negócios, qualidade interna e cobertura de testes.

## 📋 Sobre a Atividade

Cada dupla desenvolve uma solução utilizando TDD (Red-Green-Refactor) assistido por ferramentas de IA generativa. O objetivo não é apenas o código funcional, mas a análise de como a IA influencia a testabilidade, a manutenibilidade e a complexidade do código.

**Ferramentas de IA Utilizadas:**
* 🤖 **GitHub Copilot**
* ✨ **Google Gemini**

---

## 💼 Regras de Negócio (Domínio)

O sistema recebe como entrada o **Salário Bruto** (valor numérico positivo) e realiza o seguinte cálculo:

$$Salário Líquido = Salário Bruto - Desconto INSS - Desconto IR$$

### 1. Descontos Obrigatórios

* **INSS:** 8% sobre o salário bruto.
    * *Observação:* Limitado a um teto máximo de desconto (conforme configuração definida no código).
* **IRRF:**
    * **Isento:** Para salários brutos até R$ 2.000,00.
    * **Taxado:** 10% sobre o **valor total** do salário bruto para salários acima de R$ 2.000,00.

### 2. Regras Adicionais e Restrições

* ❌ **Validação:** Salários iguais ou inferiores a zero geram erro/exceção.
* math **Arredondamento:** O resultado final deve ter duas casas decimais.
* 🚫 **Restrições Técnicas:**
    * Não utilizar banco de dados.
    * Não utilizar interfaces gráficas (GUI).
    * Não utilizar APIs externas.
    * Não utilizar frameworks complexos.

---

## 📊 Atributos de Qualidade e Métricas


### Atributos Alvo
1.  **Correção Funcional:** Precisão absoluta nos cálculos de descontos.
2.  **Testabilidade:** Código desacoplado que permite testes unitários independentes.
3.  **Manutenibilidade:** Código limpo para facilitar futuras alterações de alíquotas.
4.  **Confiabilidade:** Tratamento robusto de entradas inválidas.

### Métricas de Controle

| Métrica | Meta (Target) | Justificativa |
| :--- | :--- | :--- |
| **Cobertura de Testes** | **> 90%** (Ideal: 100%) | Garante que a IA e os devs cobriram todos os cenários (ex: isenção, teto, erros). |
| **Complexidade Ciclomática** | **< 5** (por método) | Evita aninhamento excessivo de `ifs/else` na lógica de cálculo de impostos. |

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python]


---

