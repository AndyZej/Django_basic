Cvičení 4 - druhá stránka

Podle příkladu z prezentace napiš stránku, která zobrazí náhodné číslo z rozmezí mezi 0 a 100. Stránka by měla být přiřazena na adresu /random/. Stránka by měla zobrazovat Vylosované číslo: <vylosované číslo>, přičemž do správného místa vložíš vylosované číslo. Pamatuj, že metoda, která se má vykonat, by měla vracet objekt typu HttpResponse.

Tip: můžeš použít následující regulární výraz k přiřazení funkce na správnou adresu:

r'^random/$'

Můžeš také použít metodu path, pak nemusíš používat regulární výrazy.