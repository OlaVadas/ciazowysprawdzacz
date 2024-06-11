polish_food_list = [
    "jabłko", "banan", "pomarańcza", "truskawka", "borówka", "malina", "jeżyna",
    "mango", "ananas", "winogrona", "arbuz", "melon", "brzoskwinia", "śliwka",
    "nektarynka", "wiśnia", "gruszka", "kiwi", "granat", "cytryna", "limonka",
    "awokado", "pomidor", "marchew", "ogórek", "sałata", "szpinak", "jarmuż",
    "brokuł", "kalafior", "brukselka", "szparagi", "fasolka szparagowa", "groszek",
    "cukinia", "papryka", "cebula", "czosnek", "pieczarka", "ziemniak", "bataty",
    "kukurydza", "bakłażan", "dynia", "rzodkiewka", "burak", "rzepa", "pasternak",
    "seler", "fenkuł", "por", "szczypiorek", "szarlotka", "okra", "kapusta pekińska",
    "kapusta", "rzodkiew", "endywia", "rukola", "rukiew wodna", "mniszek lekarski",
    "bazylia", "kolendra", "pietruszka", "koper", "mięta", "rozmaryn", "tymianek",
    "oregano", "szałwia", "estragon", "liść laurowy", "trybula", "majeranek",
    "papryka", "pieprz cayenne", "papryczka chili", "czarny pieprz", "biały pieprz",
    "kurkuma", "imbir", "cynamon", "gałka muszkatołowa", "goździki", "ziele angielskie",
    "kardamon", "wanilia", "anyż", "nasiona kopru", "nasiona kminku", "nasiona gorczycy",
    "kolendra", "kminek", "kończyna", "szafran", "anyż gwiazdkowaty", "sumak",
    "tamarind", "macierzanka", "liście curry", "borówka", "jałowiec", "wasabi",
    "chrzan", "pieprz syczuański", "nasiona sezamu", "nasiona maku", "nasiona dyni",
    "nasiona słonecznika", "nasiona chia", "nasiona konopi", "nasiona lnu", "migdały",
    "orzechy nerkowca", "orzechy włoskie", "orzechy pekan", "orzechy laskowe",
    "pistacje", "orzechy makadamia", "orzechy brazylijskie", "orzeszki ziemne",
    "kasztany", "kokos", "komosa ryżowa", "ryż", "owies", "jęczmień", "pszenica",
    "proso", "sorgo", "gryka", "żyto", "orkisz", "amarantus", "bulgur", "kuskus",
    "polenta", "grysik", "kasza kukurydziana", "makaron", "chleb", "bułka", "bagietka",
    "brioche", "croissant", "pączek", "muffin", "bułka maślana", "pita", "tortilla",
    "naan", "focaccia", "ciabatta", "challah", "precel", "krakers", "paluszek",
    "biscuit", "ciastko", "brownie", "ciasto", "tarta", "pasztet", "eklerek",
    "makaronik", "babeczka", "sernik", "pudding", "krem", "mus", "sorbet", "gelato",
    "lody", "jogurt", "kefir", "masło", "ser", "serek śmietankowy", "ricotta",
    "twaróg", "śmietana", "bita śmietana", "crème fraîche", "mleko", "mleko migdałowe",
    "mleko sojowe", "mleko ryżowe", "mleko owsiane", "mleko kokosowe", "mleko konopne",
    "mleko kozie", "maślanka", "mleko skondensowane", "mleko odparowane", "śmietanka",
    "śmietana", "mleko pełne", "mleko odtłuszczone", "mleko półtłuste", "mleko pełnotłuste",
    "mielone mięso", "stek wołowy", "mostek wołowy", "żebra wołowe", "polędwica wołowa",
    "pieczona wołowina", "mielone wieprzowe", "schab wieprzowy", "polędwiczka wieprzowa",
    "żeberka wieprzowe", "łopatka wieprzowa", "boczek", "szynka", "kiełbasa", "hot dog",
    "pepperoni", "salami", "chorizo", "prosciutto", "pierś z kurczaka", "udo z kurczaka",
    "noga z kurczaka", "skrzydełko z kurczaka", "mielone mięso z kurczaka", "pałka z kurczaka",
    "pierś z indyka", "udo z indyka", "mielone mięso z indyka", "noga z indyka", "pierś z kaczki",
    "udo z kaczki", "pierś z gęsi", "udo z gęsi", "przepiórka", "bażant", "królik",
    "kotlety jagnięce", "polędwiczka jagnięca", "golonka jagnięca", "łopatka jagnięca",
    "mielone mięso jagnięce", "żeberka jagnięce", "dziczyzna", "wieprzowina", "drób", "łosoś",
    "tuńczyk", "pstrąg", "dorsz", "plamiak", "halibut", "makrela", "sardynki", "anchois",
    "miecznik", "marlin", "rekin", "węgorz", "tilapia", "snapper", "okoń", "sum",
    "flądra", "sola", "grander", "mahi-mahi", "żabnica", "mintaj", "sielawa", "śledź",
    "okoń", "szczupak", "sandacz", "niebieski", "drum", "leszcz", "pielęgnica", "kawior",
    "krab", "homar", "krewetka", "skorupiak", "przegrzebek", "ostrygi", "małże", "małż",
    "abalone", "ośmiornica", "kałamarnica", "cuttlefish", "ogórek morski", "jeżowiec",
    "meduza", "tuńczyk biały", "mahi-mahi", "wahoo", "bonito", "kobia", "królewski",
    "triggerfish", "tilefish", "ikra", "wodorosty", "nori", "kombu", "wakame", "arame",
    "dulse", "hijiki", "agar", "sałata morska", "spirulina", "chlorella", "jaja kurczaka",
    "jaja kaczki", "jaja przepiórcze", "jaja gęsie", "jaja strusia", "jaja indyka", "kawior",
    "ikra ryb", "ślimak", "żabie udka", "aligator", "krokodyl", "mięso kangura", "mięso wielbłąda",
    "mięso konia", "mięso kozy", "mięso królika", "mięso łosia", "mięso jelenia", "mięso bizona",
    "dzik", "dzikie indyki", "dziczyzna", "sushi", "surowe jajka", "surowe mieso", "surowe ryby",
]
