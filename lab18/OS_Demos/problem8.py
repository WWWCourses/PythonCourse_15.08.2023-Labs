# Напишете програма за достъп до променливите на средата и техните стойности.

# os.environ() –  достъп до дадена среда. Например главната директория environ[‘HOME’] е еквивалентно на getenv(“HOME”).
# оs.getenv(key, default=None) –  връща запазената стойност под зададената среда в случа параметъра key, ако съществува, иначе default ако не съществува.

import os

print(os.environ['PATH'])