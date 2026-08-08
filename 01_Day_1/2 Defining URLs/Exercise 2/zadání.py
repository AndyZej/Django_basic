Napište pohled, který je přiřazen k adrese /random/<min number>/<max number>/,
kde min number a max number by měla být čísla (zatím se nebojte o validaci –
prostě vezměte proměnnou). Tato stránka by měla zobrazit náhodné číslo z rozsahu,
který určil uživatel. Stránka by měla zobrazit text Uživateli byly zadány hodnoty
<min number> a <max number>. Následující číslo bylo vylosováno: <drawn number>,
samozřejmě s vhodným vložením proměnných na správná místa.
Všimněte si, jak se pohledy z cvičení 1, 2 nebo 3 (z předchozí sekce) vykonávají v závislosti na různém počtu parametrů.

Nápověda: Regulární výraz pro soubor urls.py

r'^random/(?P<min_number>(¯min_number)+)/(?P<max_number>(¯min_number)+)/$'

Můžete také použít metodu path, pak nebudete muset používat regulární výrazy.

'random/<int:min_number>/<int:max_number>/'