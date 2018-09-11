# selenium_automation_practice
[PT} Prática de automação de testes de software com Selenium e Python.
[EN] Software testing automation pratice with Selenium and Python.

[PT] Este repositório foi criado como parte de uma prova de teste de admissão, para automação de testes de software. Decidi usar Python com Selenium, tendo em vista a natureza flexível da linguagem Python, que me dá maior controle de programação sobre os testes, permitindo, por exemplo, selecionar produtos aleatoriamente em um site, criar listas facilmente, etc.

[EN] This repository was created as part of an admission test for software testing automation. I decided to use Python with Selenium, keeping in mind its language flexibility that gives me more programming control over the tests, allowing me to randomly select products in a given website, easily create lists, etc.

Pré-requisitos:
- ter a linguagem Python, a partir da versão 3, instalada no computador. Pode ser obtida aqui: https://www.python.org/downloads/
- ter a biblioteca Selenium devidamente instalada e configurada no computador. Siga as instruções aqui https://pypi.org/project/selenium/ ou simplesmente: execute o comando "pip install selenium" e baixe o driver do Chrome aqui https://sites.google.com/a/chromium.org/chromedriver/downloads.

Instruções:
Verifique o código-fonte. Usei como caso de teste, a compra feita por um novo cliente, que requer a entrada de  um e-mail. Assim, desenvolvi um simples gerador de e-mails que usa um arquivo para controlar quantas vezes o script já foi executado, para adicionar um número ao final, e uma variável que armazena um nome que precede este número, para evitar a tentativa de criação de e-mail já existente ao executar o teste diversas vezes. Procure pela linha 'repeated_name = "YourName"' e coloque um nome a ser concatenado no novo e-mail.


