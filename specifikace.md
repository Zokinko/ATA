Pokud je požadováno přemístění nákladu z jednoho místa do druhého, vozík si materiál vyzvedne do 1 minuty.

• UNSPECIFIED_SUBJECT - Nie je definované aké "miesto"
• UNSPECIFIED_SUBJECT - Použitie slova "náklad" vo význame slova "materiál", ktoré sa používa všade v texte
• IMPLICIT - Vyzvedne materiál, ale nie je explicitne povedané odkiaľ

*Pokud je požadováno přemístnění materiálu ze zdrojové stanice do cílové stanice, vozík si materiál vyzvedne ze zdrojové stanice do 1 minuty.*

Pokud se to nestihne, materiálu se nastavuje prioritní vlastnost.

• AMB_REFERENCE - "se to nestihne". Čo znamená "to"?

*Pokud se vyzvednutí materiálu nestihne, materiálu se nastavuje prioritní vlastnost.*

Každý prioritní materiál musí být vyzvednutý vozíkem do 1 minuty od nastavení prioritního požadavku.

• DANGLING_ELSE - Čo sa stane v prípade keď vyzdvihnutý nebude?
• AMB_SUBJECT - "prioritní materiál" je zle vyjedrený oproti predchádzajúcemu použitiu

*Každý materiál s prioritní vlastností musí být vyzvednutý vozíkem do 1 minuty od nastavení prioritního požadavku. Pokud se materiál s prioritní vlastností nevyzvedne, bude vyvolána výjimka X11.*


Pokud vozík nakládá prioritní materiál, přepíná se do režimu pouze-vykládka.

• AMB_SUBJECT - "prioritní materiál" je zle vyjedrený oproti predchádzajúcemu použitiu
• AMB_STATEMENT - "nakládá" je zle vyjedrený oproti predchádzajúcemu použitiu "vyzvedává"
• OTHER - preklep v "pouze-vykládka"

*Pokud vozík vyzvedává materiál s prioritní vlastností, přepíná se do režimu pouze-vykládá.*


V tomto režimu zůstává, dokud nevyloží všechen takový materiál.

• AMB_REFERENCE - "V tomto režimu". Čo znamená "tomto", aký je to režím?
• AMB_SUBJECT - "prioritní materiál" je zle vyjedrený oproti predchádzajúcemu použitiu
• UNSPECIFIED_SUBJECT - Kto zostáva v režíme "pouze-vykládá?

*Vozík v režimu pouze-vykládá zůstává, dokud nevyloží všechen materiál s prioritní vlastností.*


Normálně vozík během své jízdy může nabírat a vykládat další materiály v jiných zastávkách.

• AMB_STATEMENT - Čo znamená stav "normálně"?
• AMB_STATEMENT - Čo znamená vlastnosť "jiných"?
• AMB_STATEMENT - "nabírat" je zle vyjedrený oproti predchádzajúcemu použitiu "vyzvedávat"
• UNSPECIFIED_SUBJECT - "zastávkách" je zle vyjedrený oproti predchádzajúcemu použitiu "stanice"
• DANGLING_ELSE - Čo sa stane v prípade keď nebude v režime pouze-vykládá?

*Vozík v režimu pouze-vykládá, během své jízdy může pouze vykládat další materiály v cílových stanicích. Pokud není v režimu pouze-vykládá, může během své jízdy vyzvedávat i vykládat v stanicích.*


Na jednom místě může vozík akceptovat nebo vyložit jeden i více materiálů.

• UNSPECIFIED_SUBJECT - "místě" je zle vyjedrený oproti predchádzajúcemu použitiu "stanice"
• AMB_STATEMENT - "akceptovat" je zle vyjedrený oproti predchádzajúcemu použitiu "vyzvedávat"

*V jedné stanici může vozík vyzvedávat nebo vyložit jeden i více materiálů.*

Pořadí vyzvednutí materiálů nesouvisí s pořadím vytváření požadavků.

*Pořadí vyzvednutí materiálů nesouvisí s pořadím vytváření požadavků.*


Vozík neakceptuje materiál, pokud jsou všechny jeho sloty obsazené nebo by jeho převzetím byla překročena maximální nosnost.

• AMB_STATEMENT - "neakceptuje" je zle vyjedrený oproti predchádzajúcemu použitiu "nevyzvedává"
• AMB_STATEMENT - "převzetím" je zle vyjedrený oproti predchádzajúcemu použitiu "vyzvednutím"

*Vozík nevyzvedává materiál, pokud jsou všechny jeho sloty obsazené nebo by jeho vyzvednutím byla překročena maximální nosnost.*