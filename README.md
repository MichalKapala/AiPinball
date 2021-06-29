# AiPinball
##### Projekt prostej, klasycznej gry pinball z przeciwnikiem w postaci sztucznej inteligencji.

##### Pliki:
**pinball.py**- Moduł zawiera główny silnik gry. Klasa ```python Rectangle()``` reprezentująca graczy oraz klasa ```python Ball()``` reprezentująca piłkę. Sa one odpowiedzialne za mechanike gry.

**data_collect.py**- W tym module znajduję się petla główna oraz funkja odpowiedzialna za zapis potrzebnych danych do późniejszego uczenia modelu.

**AI.py**- Implementacja modelu uczenai maszynowego. Model zostaje przeuczony na wcześniej zebranych danych (w trybie gry 'test')

**ruch.data**- Dane potrzebne do przeuczenia modelu

##### Tryby gry:
1. **test**- tryb gry w którym nie są liczone punkty i nie da się skuć. Ruch wyonuje tylko jeden gracz aby zebrać potrzebne dane do wyuczenia modelu.
2. **AI**- tryb możliwy dopiero po zebraniu danych uczących. Gracz gra przeciwko AI.
3. **AIvAI**- Możliwość obserwacji walki dwóch róznych modeli przeuczonych na identycznych danych.
4. **1v1**- Możliwość gry przeciwko ludzkiemu przeiwnikowi.

