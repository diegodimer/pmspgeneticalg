Para rodar o algoritmo você precisa:
Ir até a pasta da meta-heurística e rodar o seguinte comando:
>> python3 PMSPMain.py <arquivo de instancia> <tamanho da populacao> <max iteracoes> <seed/opcional>

OU

no arquivo example.py tem um exemplo de como rodar a instância desejada pela IDE/sem usar linha de comando

Incluímos na pasta da meta-heurística uma instância para testes, mas o algoritmo funciona com qualquer instância no formato disponibilizado no moodle.

-----

Os logs das execuções do GLPK encontram-se na pasta LOGS. Eles foram gerados na busca pela relaxação linear das instâncias.
Junto, na pasta LOGS, existe um arquivo chamado "RUN", ele é um script criado para rodar todas as instâncias (as converte para a nossa formulação, depois executa o glpk com limite de 1 hora escrevendo logs no arquivo terminado em LOG.sol). Para rodá-lo, basta digitiar "bash RUN"

-----

O desenvolvimento do relatório e dos slides foi na plataforma overleaf, o link para o documento: https://www.overleaf.com/read/ppcdcvsdtvkd
As ilustrações utilizadas no relatório foram desenvolvidas pelo grupo com o auxilio do site: https://www.mathcha.io
A meta-heurística foi desenvolvida com o auxílio do versionamento do github, em um repositório privado.

---

O trabalho foi desenvolvido no sistema operacional LINUX, não tendo garantia de funcionamento em Windows ou Mac.



