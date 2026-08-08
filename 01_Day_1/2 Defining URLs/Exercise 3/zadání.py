Cvičení 3
Napiš pohled, který je přiřazen k adrese /hello/<name>/,
kde name by měl být řetězec (zatím se neboj validace - prostě vezmi proměnnou).
Tato stránka by měla zobrazovat hello <name>,
samozřejmě vložením vhodné proměnné na správné místo.

Nápověda: Regulární výraz pro soubor urls.py

r'^hello/(?P<name>([A-Za-z])+)/$'

Můžeš také použít metodu path, pak nebudeš muset používat regulární výrazy.

'random/<str:name>/'