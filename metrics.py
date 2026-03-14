from evaluate import load

# 1. Renomeie a variável da métrica para algo diferente da função
metric_bertscore = load("bertscore")

def calculate_bertscore(pred_code, ref_code):
    # 2. Use a variável correta aqui
    results = metric_bertscore.compute(
        predictions=[pred_code], 
        references=[ref_code], 
        model_type="microsoft/codebert-base",
        num_layers=12
    )
    return results['f1'][0]
    
# Código gerado pelo seu agente
code = """
#include <iostream>
int main() {
    int a = 10;
    int b = 20;
    std::cout << "Soma: " << a + b << std::endl;
    return 0;
}
"""

# Código de referência (Gabarito)
code2 = """
#include <iostream>
using namespace std;
int main() {
    int x = 10, y = 20;
    cout << x + y << endl;
    return 0;
}
"""

# 3. Chame a função pelo novo nome
score = calculate_bertscore(code, code2)
print(f"Similaridade Semântica do Arquivo: {score:.4f}")