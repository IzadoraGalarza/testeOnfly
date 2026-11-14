# Entrega
# Izadora Galarza Alves
## Defeitos que corrigi

**1. Câmbio** (`services/currency_converter.py`)
Reserva em dólar saía com valor errado (100 USD virava 18,45 em vez de 542,00). O código dividia pela taxa em vez de multiplicar.

**2. Noites** (`services/stay_calculator.py`)
Em reserva que virava o mês, o resultado saía negativo (30/01 até 02/02 dava -28). O cálculo usava só o dia do mês, e não a diferença entre as datas inteiras, então tirei o .day e coloquei .days para fora do parenteses.

**3. Status** (`services/status_policy.py`)
Reserva NO_SHOW entrava nos totais. A regra só excluía CANCELLED. Agora só CONFIRMED é faturável.

**4. Top hotéis** (`services/report_builder.py`)
O ranking saía do menor para o maior valor, porque o `sorted` estava em ordem crescente. Neguei o valor na `key` para ficar decrescente, e o desempate por `hotel_id` continua crescente.

## Como cheguei neles

Rodei o `pytest -q` e deram 5 falhas. Em cada uma li o teste, achei a regra no README e usei os números do erro como pista. No câmbio, por exemplo, 118,45 menos 100 dá 18,45, que é 100 dividido por 5,42, então vi que era divisão. No das noites, o -28 veio de usar só o dia do mês. Depois abri o arquivo responsável por cada regra e comparei com o README.

[ ] Depois rodei a amostra (`exemplo-validacao.csv`) e comparei com a tabela do README.
[ ] Rodei também com `reservas_hoteis.csv` e conferi se os números fecham entre si.

## Como validar

```
python -m venv .venv
.venv\Scripts\Activate.ps1      (Linux/Mac: source .venv/bin/activate)
pip install -r requirements-dev.txt
pytest -q
```

Para gerar o relatório (no PowerShell, antes rode `$env:PYTHONPATH="src"`):

```
PYTHONPATH=src python -m onfly_report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json
```

## Resultado

pytest: [ ] '5 passed in 1.11s'
Amostra: [ ] Bateu corretamente com os dados
