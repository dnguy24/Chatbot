## intent:greet
- hey
- hello there
- hi
- hello there
- good morning
- good evening
- moin
- hey there
- let's go
- hey dude
- how's it going
- goodmorning
- goodevening
- good afternoon
- what's up

## intent:goodbye
- i gotta go
- cu
- good by
- cee you later
- good night
- good afternoon
- bye
- goodbye
- have a nice day
- see you around
- bye bye
- see you later

##intent: ask_weather
- What's the [weather today](weather:today)?
- How hot is it [today](weather:today)?
- How's the [weather](weather:today)?
- What's the [temperature in Rochester](weather:today)?
- Is it cold [today](weather:today)?
- Is it a [beautiful day today](weather:today)?
- What is the [forecast for today](weather:today)?
- What is the [forecast for tomorrow](weather:tomorrow)
- How's the weather [tomorrow](weather:tomorrow)

##synonym:tomorrow
- tmr
- tomorrow
- tomorow

##synonym:today
- now
- today
- 2day
- right now

##intent: hungry
- I'm hungry
- I need something to eat
- Is there any dining place open right now?
- Is [Douglass](dininghall:douglass) open?
- Can I go to [Douglass Dining](dininghall:douglass)?
- Is [The Pit](dininghall:wilson) open?
- Is [Danforth](dininghall:dfo) open?
- Is [Optikale](dininghall:goergen) open?
- Can I go to [DFO](dininghall:dfo) right now?
- Is [Danforth](dininghall:dfo) open?
- I need a [burrito bowl](dininghall:wilson) right now
- I want a [burrito bowl](dininghall:wilson)
- I want to eat at [Wok](dininghall:wilson)
- Can I eat at [douglass](dininghall:douglass) now?
- Can I go to [pit](dininghall:wilson) now?
- Can I go to [optikale](dininghall:goergen)?
- Is [Hillside](dininghall:hillside) open?
- Can I go to [hillside](dininghall:hillside) now?
- Is [Starbuck's](dininghall:starbucks) open?
- Can I go to [Starbucks](dininghall:starbucks) now?
- Is [Peet's](dininghall:peets) still open?
- Is [peets](dininghall:peets) still open?
- Is [peet's](dininghall:peets) open?
- Is [peet's](dininghall:peets) open?
- Can I go to [peet's](dininghall:peets)?
- Can I go to [Peet](dininghall:peets)?
- Can I go to [peets](dininghall:peets) now?
- Is [Peet's Coffee](dininghall:peets) open now?
- Can I go to [peets coffee](dininghall:peets) now?
- Is [peet's](dininghall:peets) still open
- Is [Grab and go](dininghall:grabngo) open?
- Is [Rocky's Sub Shop](dininghall:rockys) open?
- I want a [Sandwich](dininghall:rockys)
- Is [Rocky's](dininghall:rockys) still open?
- Can I eat at [Rocky](dininghall:rockys)?
- Can I eat at [Rockies](dininghall:rockys)?
- Is [Southside Market](dininghall:southside) open?
- Is [Connections'](dininghall:connections) open?
- Can I go to [Faculty Club](dininghall:faculty) now?
- Is [The Cave](dininghall:cave) open?
## synonym:southside
- Southside Market
- Southside
- south side

## regex: dininghall
- (?<!^)(?<![,:])' " (?![,:])(?!$)

## synonym:rockys
- Rocky's Sub shop
- Sandwich place
- Rockys
- Rockies
- Sandwich
- Rocky's
- Rocky

## synonym:starbucks
- SB
- Starbucks
- Starbuck's
- Starbuck

## synonym:peets
- Peet's Coffee
- Peets
- Pits
- peet's
- peets

## synonym:grabngo
- Grab & Go
- Grab n go
- grab and go

## synonym:douglass
- Douggie
- Douglass dining hall
- Frederick Douglass Commons
- Frederick Douglass
- Douglass Dining
- douglass still
- Douglass still
## intent:ask_directions
- How do I get to [Gilbert](directions:gilbert) from [Gilbert](directions:gilbert)
- What is the direction from [Gilbert](directions:gilbert) to [Gilbert](directions:gilbert)?
- How do I get to [Tiernan](directions:tiernan) from [Tiernan](directions:tiernan)
- What is the direction from [Tiernan](directions:tiernan) to [Tiernan](directions:tiernan)?
- How do I get to [Hoeing](directions:hoeing) from [Hoeing](directions:hoeing)
- What is the direction from [Hoeing](directions:hoeing) to [Hoeing](directions:hoeing)?
- How do I get to [Lovejoy](directions:lovejoy) from [Lovejoy](directions:lovejoy)
- What is the direction from [Lovejoy](directions:lovejoy) to [Lovejoy](directions:lovejoy)?
- How do I get to [Wilson](directions:wilson) from [Wilson](directions:wilson)
- What is the direction from [Wilson](directions:wilson) to [Wilson](directions:wilson)?
- How do I get to [Rettner](directions:rettner) from [Rettner](directions:rettner)
- What is the direction from [Rettner](directions:rettner) to [Rettner](directions:rettner)?
- How do I get to [Crosby](directions:crosby) from [Crosby](directions:crosby)
- What is the direction from [Crosby](directions:crosby) to [Crosby](directions:crosby)?
- How do I get to [Burton](directions:burton) from [Burton](directions:burton)
- What is the direction from [Burton](directions:burton) to [Burton](directions:burton)?
- How do I get to [Lechase](directions:lechase) from [Lechase](directions:lechase)
- What is the direction from [Lechase](directions:lechase) to [Lechase](directions:lechase)?
- How do I get to [Rush rhees](directions:rushrhees) from [Rush-rhees](directions:rushrhees)
- What is the direction from [Rush-rhees](directions:rushrhees) to [Rush-rhees](directions:rushrhees)?
- How do I get to [B&l](directions:bl) from [Bausch & Lomb](directions:bl)
- What is the direction from [Bl](directions:bl) to [Bausch and lomb](directions:bl)?
- How do I get to [Dewey](directions:dewey) from [Dewey](directions:dewey)
- What is the direction from [Dewey](directions:dewey) to [Dewey](directions:dewey)?
- How do I get to [Lattimore](directions:lattimore) from [Lattimore](directions:lattimore)
- What is the direction from [Lattimore](directions:lattimore) to [Lattimore](directions:lattimore)?
- How do I get to [Morey](directions:morey) from [Morey](directions:morey)
- What is the direction from [Morey](directions:morey) to [Morey](directions:morey)?
- How do I get to [Its](directions:its) from [Its](directions:its)
- What is the direction from [Its](directions:its) to [Its](directions:its)?
- How do I get to [Meliora](directions:meliora) from [Meliora](directions:meliora)
- What is the direction from [Meliora](directions:meliora) to [Meliora](directions:meliora)?
- How do I get to [Harkness](directions:harkness) from [Harkness](directions:harkness)
- What is the direction from [Harkness](directions:harkness) to [Harkness](directions:harkness)?
- How do I get to [Gavett](directions:gavett) from [Gavett](directions:gavett)
- What is the direction from [Gavett](directions:gavett) to [Gavett](directions:gavett)?
- How do I get to [Gleason](directions:gleason) from [Gleason](directions:gleason)
- What is the direction from [Gleason](directions:gleason) to [Gleason](directions:gleason)?
- How do I get to [Simon](directions:simon) from [Simon](directions:simon)
- What is the direction from [Simon](directions:simon) to [Simon](directions:simon)?
- How do I get to [Wallis](directions:wallis) from [Wallis](directions:wallis)
- What is the direction from [Wallis](directions:wallis) to [Wallis](directions:wallis)?
- How do I get to [Hopeman](directions:hopeman) from [Hopeman](directions:hopeman)
- What is the direction from [Hopeman](directions:hopeman) to [Hopeman](directions:hopeman)?
- How do I get to [Hoyt](directions:hoyt) from [Hoyt](directions:hoyt)
- What is the direction from [Hoyt](directions:hoyt) to [Hoyt](directions:hoyt)?
- How do I get to [Hutch](directions:hutch) from [Hutch](directions:hutch)
- What is the direction from [Hutchison](directions:hutch) to [Hutch](directions:hutch)?
- How do I get to [Hylan](directions:hylan) from [Hylan](directions:hylan)
- What is the direction from [Hylan](directions:hylan) to [Hylan](directions:hylan)?
- How do I get to [Wilmot](directions:wilmot) from [Wilmot](directions:wilmot)
- What is the direction from [Wilmot](directions:wilmot) to [Wilmot](directions:wilmot)?
- How do I get to [Goergen](directions:goergen) from [Goergen](directions:goergen)
- What is the direction from [Optikale](directions:goergen) to [Goergen](directions:goergen)?
- How do I get to [basketball courts](directions:gym) from [Goergen athletic center](directions:gym)
- What is the direction from [gym](directions:gym) to [GAC](directions:gym)?
- How do I get to [Uhs](directions:uhs) from [Uhs](directions:uhs)
- What is the direction from [Uhs](directions:uhs) to [Uhs](directions:uhs)?
- How do I get to [Danforth](directions:dfo) from [Sueb](directions:sueb)
- What is the direction from [Hillside](directions:hillside) to [Sueb](directions:sueb)?
- How do I get to [Spurrier](directions:spurrier) from [Spurrier](directions:spurrier)
- What is the direction from [Spurrier](directions:spurrier) to [Spurrier](directions:spurrier)?
- How do I get to [Sage](directions:sage) from [Sage](directions:sage)
- What is the direction from [Sage](directions:sage) to [Sage](directions:sage)?
- How do I get to [Wilder](directions:wilder) from [Wilder](directions:wilder)
- What is the direction from [Wilder](directions:wilder) to [Wilder](directions:wilder)?
- How do I get to [Anderson](directions:anderson) from [Anderson](directions:anderson)
- What is the direction from [Anderson](directions:anderson) to [Anderson](directions:anderson)?
- How do I get to [Obrien](directions:obrien) from [Obrien](directions:obrien)
- What is the direction from [Obrien](directions:obrien) to [Obrien](directions:obrien)?
- How do I get to [Csb](directions:csb) from [Csb](directions:csb)
- What is the direction from [Csb](directions:csb) to [Csb](directions:csb)?



## synonym:goergen
- Optikale
- Goergen
- Opti
- Green stuff

##intent:ask_library
- Where can I study?
- What are the libraries opening right now?
- Library
- Libraries
- I need the libraries information
- I need to go to the library


##intent:ask_coffee
- Where can I grab a coffee?
- I need some caffeine
- Where are the cafe places
- Coffee
- Caffeine
- I need a coffee
- I am so sleepy
- Where are the cafes on campus

## synonym:wilson
- Wilson
- The Pit
- Pit
- pit
- Wok
- Burrito Bowl
- Wilson Commons

##intent:thankyou
- Thanks
- That was some great help
- Thanx
- Tks
- Thank you for your help
- Thank you so much
- You are a great help

## synonym:rushrhees
- Rush-rhees library
- Rush rhees
- Rush rhee library
- Connections

## synonym:obrien
- O'Brien
- Obrien
- O' Brien
- Jackson Court

##intent:inform_starting_location
- I need to go there from [Gilbert](destinations:gilbert)
- From[Gilbert](destinations:gilbert), please
- [Gilbert](destinations:gilbert)
- I wanna go there from [Gilbert](destinations:gilbert)
- From[Tiernan](destinations:tiernan), please
- [Tiernan](destinations:tiernan)
- I wanna go there from [Tiernan](destinations:tiernan)
- From[Hoeing](destinations:hoeing), please
- [Hoeing](destinations:hoeing)
- I wanna go there from [Hoeing](destinations:hoeing)
- From[Lovejoy](destinations:lovejoy), please
- [Lovejoy](destinations:lovejoy)
- I wanna go there from [Lovejoy](destinations:lovejoy)
- From[Wilson](destinations:wilson), please
- [Wilson](destinations:wilson)
- I wanna go there from [Wilson](destinations:wilson)
- From[Rettner](destinations:rettner), please
- [Rettner](destinations:rettner)
- I wanna go there from [Rettner](destinations:rettner)
- From[Crosby](destinations:crosby), please
- [Crosby](destinations:crosby)
- I wanna go there from [Crosby](destinations:crosby)
- From[Burton](destinations:burton), please
- [Burton](destinations:burton)
- I wanna go there from [Burton](destinations:burton)
- From[Lechase](destinations:lechase), please
- [Lechase](destinations:lechase)
- I wanna go there from [Lechase](destinations:lechase)
- From[Rush-rhees](destinations:rushrhees), please
- [Rush rhees](destinations:rushrhees)
- I wanna go there from [Connections](destinations:rushrhees)
- From[B&l](destinations:bl), please
- [B&l](destinations:bl)
- I wanna go there from [B&l](destinations:bl)
- From[Dewey](destinations:dewey), please
- [Dewey](destinations:dewey)
- I wanna go there from [Dewey](destinations:dewey)
- From[Lattimore](destinations:lattimore), please
- [Lattimore](destinations:lattimore)
- I wanna go there from [Lattimore](destinations:lattimore)
- From[Morey](destinations:morey), please
- [Morey](destinations:morey)
- I wanna go there from [Morey](destinations:morey)
- From[Its](destinations:its), please
- [Its](destinations:its)
- I wanna go there from [Its](destinations:its)
- From[Meliora](destinations:meliora), please
- [Meliora](destinations:meliora)
- I wanna go there from [Meliora](destinations:meliora)
- From[Harkness](destinations:harkness), please
- [Harkness](destinations:harkness)
- I wanna go there from [Harkness](destinations:harkness)
- From[Gavett](destinations:gavett), please
- [Gavett](destinations:gavett)
- I wanna go there from [Gavett](destinations:gavett)
- From[Gleason](destinations:gleason), please
- [Gleason](destinations:gleason)
- I wanna go there from [Gleason](destinations:gleason)
- From[Simon](destinations:simon), please
- [Simon](destinations:simon)
- I wanna go there from [Simon](destinations:simon)
- From[Wallis](destinations:wallis), please
- [Wallis](destinations:wallis)
- I wanna go there from [Wallis](destinations:wallis)
- From[Hopeman](destinations:hopeman), please
- [Hopeman](destinations:hopeman)
- I wanna go there from [Hopeman](destinations:hopeman)
- From[Hoyt](destinations:hoyt), please
- [Hoyt](destinations:hoyt)
- I wanna go there from [Hoyt](destinations:hoyt)
- From[Hutch](destinations:hutch), please
- [Hutch](destinations:hutch)
- I wanna go there from [Hutch](destinations:hutch)
- From[Hylan](destinations:hylan), please
- [Hylan](destinations:hylan)
- I wanna go there from [Hylan](destinations:hylan)
- From[Wilmot](destinations:wilmot), please
- [Wilmot](destinations:wilmot)
- I wanna go there from [Wilmot](destinations:wilmot)
- From[Goergen](destinations:goergen), please
- [Goergen](destinations:goergen)
- I wanna go there from [Goergen](destinations:goergen)
- From[GAC](destinations:gym), please
- [Gym](destinations:gym)
- I wanna go there from [the gym](destinations:gym)
- From[Uhs](destinations:uhs), please
- [Uhs](destinations:uhs)
- I wanna go there from [Uhs](destinations:uhs)
- From[Sueb](destinations:sueb), please
- [Sueb](destinations:sueb)
- I wanna go there from [Sueb](destinations:sueb)
- From[Spurrier](destinations:spurrier), please
- [Spurrier](destinations:spurrier)
- I wanna go there from [Spurrier](destinations:spurrier)
- From[Sage](destinations:sage), please
- [Sage](destinations:sage)
- I wanna go there from [Sage](destinations:sage)
- From[Wilder](destinations:wilder), please
- [Wilder](destinations:wilder)
- I wanna go there from [Wilder](destinations:wilder)
- From[Anderson](destinations:anderson), please
- [Anderson](destinations:anderson)
- I wanna go there from [Anderson](destinations:anderson)
- From[Obrien](destinations:obrien), please
- [Obrien](destinations:obrien)
- I wanna go there from [O' Brien](destinations:obrien)
- From[Csb](destinations:csb), please
- [Csb](destinations:csb)
- I wanna go there from [Csb](destinations:csb)
- I wanna get there from [Bausch & Lomb](destinations:bl)
- From [Douglass](destinations:douglass)
- I wanna get there from [Frederick Douglass Commons](destinations:douglass)
- [Hoyt](destinations:hoyt)
- [B&L](destinations:bl)
- [Sue B](destinations:sueb)

##synonym:csb
- CSB
- csb
- Computer Science Building

##intent:ask_directions_start_missing
- How do I get to [Gilbert](destinations:gilbert)?
- What is the way to [Gilbert](destinations:gilbert)?
- I need to get to [Gilbert](destinations:gilbert)
- How do I get to [Tiernan](destinations:tiernan)?
- What is the way to [Tiernan](destinations:tiernan)?
- I need to get to [Tiernan](destinations:tiernan)
- How do I get to [Hoeing](destinations:hoeing)?
- What is the way to [Hoeing](destinations:hoeing)?
- I need to get to [Hoeing](destinations:hoeing)
- How do I get to [Lovejoy](destinations:lovejoy)?
- What is the way to [Lovejoy](destinations:lovejoy)?
- I need to get to [Lovejoy](destinations:lovejoy)
- How do I get to [Wilson](destinations:wilson)?
- What is the way to [Wilson](destinations:wilson)?
- I need to get to [Wilson](destinations:wilson)
- How do I get to [Rettner](destinations:rettner)?
- What is the way to [Rettner](destinations:rettner)?
- I need to get to [Rettner](destinations:rettner)
- How do I get to [Crosby](destinations:crosby)?
- What is the way to [Crosby](destinations:crosby)?
- I need to get to [Crosby](destinations:crosby)
- How do I get to [Burton](destinations:burton)?
- What is the way to [Burton](destinations:burton)?
- I need to get to [Burton](destinations:burton)
- How do I get to [Lechase](destinations:lechase)?
- What is the way to [Lechase](destinations:lechase)?
- I need to get to [Lechase](destinations:lechase)
- How do I get to [Rush rhees](destinations:rushrhees)?
- What is the way to [Rush-rhees](destinations:rushrhees)?
- I need to get to [Connections](destinations:rushrhees)
- How do I get to [B&l](destinations:bl)?
- What is the way to [BL](destinations:bl)?
- I need to get to [Bausch Lomb](destinations:bl)
- How do I get to [Dewey](destinations:dewey)?
- What is the way to [Dewey](destinations:dewey)?
- I need to get to [Dewey](destinations:dewey)
- How do I get to [Lattimore](destinations:lattimore)?
- What is the way to [Lattimore](destinations:lattimore)?
- I need to get to [Lattimore](destinations:lattimore)
- How do I get to [Morey](destinations:morey)?
- What is the way to [Morey](destinations:morey)?
- I need to get to [Morey](destinations:morey)
- How do I get to [Its](destinations:its)?
- What is the way to [Its](destinations:its)?
- I need to get to [Its](destinations:its)
- How do I get to [Meliora](destinations:meliora)?
- What is the way to [Meliora](destinations:meliora)?
- I need to get to [Meliora](destinations:meliora)
- How do I get to [Harkness](destinations:harkness)?
- What is the way to [Harkness](destinations:harkness)?
- I need to get to [Harkness](destinations:harkness)
- How do I get to [Gavett](destinations:gavett)?
- What is the way to [Gavett](destinations:gavett)?
- I need to get to [Gavett](destinations:gavett)
- How do I get to [Gleason](destinations:gleason)?
- What is the way to [Gleason](destinations:gleason)?
- I need to get to [Gleason](destinations:gleason)
- How do I get to [Simon](destinations:simon)?
- What is the way to [Simon](destinations:simon)?
- I need to get to [Simon](destinations:simon)
- How do I get to [Wallis](destinations:wallis)?
- What is the way to [Wallis](destinations:wallis)?
- I need to get to [Wallis](destinations:wallis)
- How do I get to [Hopeman](destinations:hopeman)?
- What is the way to [Hopeman](destinations:hopeman)?
- I need to get to [Hopeman](destinations:hopeman)
- How do I get to [Hoyt](destinations:hoyt)?
- What is the way to [Hoyt](destinations:hoyt)?
- I need to get to [Hoyt](destinations:hoyt)
- How do I get to [Hutchison](destinations:hutch)?
- What is the way to [Hutch](destinations:hutch)?
- I need to get to [Hutch](destinations:hutch)
- How do I get to [Hylan](destinations:hylan)?
- What is the way to [Hylan](destinations:hylan)?
- I need to get to [Hylan](destinations:hylan)
- How do I get to [Wilmot](destinations:wilmot)?
- What is the way to [Wilmot](destinations:wilmot)?
- I need to get to [Wilmot](destinations:wilmot)
- How do I get to [Goergen](destinations:goergen)?
- What is the way to [Goergen](destinations:goergen)?
- I need to get to [Goergen](destinations:goergen)
- How do I get to [GAC](destinations:gym)?
- What is the way to [Goergen athletic center](destinations:gym)?
- I need to get to [the gym](destinations:gym)
- I need to go to [the basketball courts](destinations:gym)
- How do I get to [Uhs](destinations:uhs)?
- What is the way to [Uhs](destinations:uhs)?
- I need to get to [Uhs](destinations:uhs)
- How do I get to [Sueb](destinations:sueb)?
- What is the way to [Sue B](destinations:sueb)?
- What is the way to [dfo](destinations:dfo)
- I need to get to [Susan B Anthony Hall](destinations:sueb)
- I need to get to [Susan B. Anthony](destinations:sueb)
- How do I get to [Spurrier](destinations:spurrier)?
- What is the way to [Spurrier](destinations:spurrier)?
- I need to get to [Spurrier](destinations:spurrier)
- How do I get to [Sage](destinations:sage)?
- What is the way to [Sage](destinations:sage)?
- I need to get to [Sage](destinations:sage)
- How do I get to [Wilder](destinations:wilder)?
- What is the way to [Wilder](destinations:wilder)?
- How do I get to [Anderson](destinations:anderson)?
- What is the way to [Anderson](destinations:anderson)?
- I need to get to [Anderson](destinations:anderson)
- How do I get to [O' Brien](destinations:obrien)?
- What is the way to [Obrien](destinations:obrien)?
- I need to get to [Jackson Court](destinations:obrien)
- How do I get to [Csb](destinations:csb)?
- What is the way to [Csb](destinations:csb)?
- I need to get to [Csb](destinations:csb)
- How do I get to [Douglass](destinations:douglass)
- What is the way to [Douggie](destinations:douglass)
- I need to get to [Douglass Dining Hall](destinations:douglass)
- I wanna go to [Frederick Douglass Commons](destinations:douglass)

## lookup:destinations
- Hoyt
- Anderson
- Meliora
- Dewey
- O'Brien
- Susan B Anthony
- Gilbert
- Hoeing

## synonym:gym
- GAC
- Goergen Athletic Center
- gym
- basketball courts

##synonym:dfo
- Danforth
- DFO
- dfo
- Danforth Dining Hall
##synonym:sueb
- susan
- Susan B. Anthony
- Susan B Anthony Hall
- Sue B
- sueb
- sue b
- Susan B
##synonym:hillside
- Hillside
- hillside market


