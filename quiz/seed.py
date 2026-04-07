import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_cinema.settings')
django.setup()
from quiz.models import Question

# 🔥 reset
Question.objects.all().delete()

questions = [
    # --- RÉALISATEURS ---
    ("Qui a réalisé Inception ?", "Christopher Nolan", ["Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", "Martin Scorsese"]),
    ("Qui a réalisé Pulp Fiction ?", "Quentin Tarantino", ["Christopher Nolan", "Quentin Tarantino", "Martin Scorsese", "Stanley Kubrick"]),
    ("Qui a réalisé Avatar ?", "James Cameron", ["Christopher Nolan", "James Cameron", "Steven Spielberg", "Stanley Kubrick"]),
    ("Qui a réalisé Schindler's List ?", "Steven Spielberg", ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola", "Roman Polanski"]),
    ("Qui a réalisé 2001 : L'Odyssée de l'espace ?", "Stanley Kubrick", ["Steven Spielberg", "Ridley Scott", "Stanley Kubrick", "George Lucas"]),
    ("Qui a réalisé Le Parrain ?", "Francis Ford Coppola", ["Martin Scorsese", "Francis Ford Coppola", "Sidney Lumet", "Brian De Palma"]),
    ("Qui a réalisé Les Temps modernes ?", "Charlie Chaplin", ["Buster Keaton", "Charlie Chaplin", "Harold Lloyd", "Fritz Lang"]),
    ("Qui a réalisé Metropolis ?", "Fritz Lang", ["Fritz Lang", "F.W. Murnau", "Ernst Lubitsch", "G.W. Pabst"]),
    ("Qui a réalisé Psychose ?", "Alfred Hitchcock", ["Alfred Hitchcock", "Billy Wilder", "John Ford", "Orson Welles"]),
    ("Qui a réalisé Citizen Kane ?", "Orson Welles", ["John Huston", "Orson Welles", "Howard Hawks", "Frank Capra"]),
    ("Qui a réalisé La Dolce Vita ?", "Federico Fellini", ["Michelangelo Antonioni", "Federico Fellini", "Luchino Visconti", "Roberto Rossellini"]),
    ("Qui a réalisé Parasite ?", "Bong Joon-ho", ["Park Chan-wook", "Bong Joon-ho", "Kim Jee-woon", "Lee Chang-dong"]),
    ("Qui a réalisé Mad Max: Fury Road ?", "George Miller", ["Ridley Scott", "James Cameron", "George Miller", "Christopher Nolan"]),
    ("Qui a réalisé La La Land ?", "Damien Chazelle", ["Darren Aronofsky", "Damien Chazelle", "Barry Jenkins", "David Fincher"]),
    ("Qui a réalisé Fight Club ?", "David Fincher", ["David Fincher", "Darren Aronofsky", "Paul Thomas Anderson", "Spike Jonze"]),

    # --- ACTEURS / ACTRICES ---
    ("Qui joue Iron Man dans le MCU ?", "Robert Downey Jr.", ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo"]),
    ("Qui joue Forrest Gump ?", "Tom Hanks", ["Tom Hanks", "Kevin Costner", "John Travolta", "Robin Williams"]),
    ("Qui joue Jack Dawson dans Titanic ?", "Leonardo DiCaprio", ["Brad Pitt", "Leonardo DiCaprio", "Johnny Depp", "Matt Damon"]),
    ("Qui joue Hannibal Lecter dans Le Silence des agneaux ?", "Anthony Hopkins", ["Anthony Hopkins", "Jack Nicholson", "Dustin Hoffman", "Al Pacino"]),
    ("Qui joue Neo dans Matrix ?", "Keanu Reeves", ["Laurence Fishburne", "Keanu Reeves", "Hugo Weaving", "Will Smith"]),
    ("Qui joue Katniss Everdeen dans Hunger Games ?", "Jennifer Lawrence", ["Shailene Woodley", "Jennifer Lawrence", "Emma Watson", "Saoirse Ronan"]),
    ("Qui joue James Bond dans Casino Royale (2006) ?", "Daniel Craig", ["Pierce Brosnan", "Daniel Craig", "Timothy Dalton", "Sean Connery"]),
    ("Qui joue Clarice Starling dans Le Silence des agneaux ?", "Jodie Foster", ["Jodie Foster", "Meryl Streep", "Sigourney Weaver", "Glenn Close"]),
    ("Qui joue le Joker dans The Dark Knight ?", "Heath Ledger", ["Joaquin Phoenix", "Heath Ledger", "Jack Nicholson", "Jared Leto"]),
    ("Qui joue Wolverine dans X-Men ?", "Hugh Jackman", ["Hugh Jackman", "Chris Pratt", "Ryan Reynolds", "Christian Bale"]),
    ("Qui joue Hermione Granger dans Harry Potter ?", "Emma Watson", ["Emma Watson", "Keira Knightley", "Natalie Portman", "Anne Hathaway"]),
    ("Qui joue T'Challa dans Black Panther ?", "Chadwick Boseman", ["Idris Elba", "Chadwick Boseman", "Michael B. Jordan", "Mahershala Ali"]),
    ("Qui joue Scarlett O'Hara dans Autant en emporte le vent ?", "Vivien Leigh", ["Vivien Leigh", "Katharine Hepburn", "Ingrid Bergman", "Bette Davis"]),
    ("Qui joue E.T. la mère dans E.T. l'extra-terrestre ?", "Dee Wallace", ["Mary Steenburgen", "Dee Wallace", "Teri Garr", "Glenn Close"]),
    ("Qui joue Ripley dans Alien ?", "Sigourney Weaver", ["Sigourney Weaver", "Jamie Lee Curtis", "Linda Hamilton", "Jodie Foster"]),

    # --- CITATIONS CULTES ---
    ("Dans quel film entend-on 'Hasta la vista, baby' ?", "Terminator 2", ["Terminator 2", "Predator", "RoboCop", "Total Recall"]),
    ("Dans quel film dit-on 'Je suis ton père' ?", "Star Wars V", ["Star Wars IV", "Star Wars V", "Star Wars VI", "Star Wars III"]),
    ("Dans quel film dit-on 'Vous allez avoir besoin d'un plus grand bateau' ?", "Les Dents de la mer", ["Les Dents de la mer", "Moby Dick", "Piranha", "L'Abîme"]),
    ("Dans quel film entend-on 'Allons-y, Alonso !' ?", "Retour vers le futur", ["Ghostbusters", "Retour vers le futur", "Indiana Jones", "Gremlins"]),
    ("Dans quel film dit-on 'La vie, c'est comme une boîte de chocolats' ?", "Forrest Gump", ["Forrest Gump", "Cast Away", "Philadelphia", "Big"]),
    ("Dans quel film entend-on 'Tu ne peux pas gérer la vérité !' ?", "Des hommes d'honneur", ["Des hommes d'honneur", "Philadelphia", "JFK", "Nixon"]),
    ("Dans quel film dit-on 'I see dead people' ?", "Sixième Sens", ["Sixième Sens", "Poltergeist", "The Others", "Shining"]),

    # --- ANNÉES 20-50 (Cinéma classique) ---
    ("Quel film de 1927 est souvent cité comme premier film parlant ?", "Le Chanteur de jazz", ["Le Chanteur de jazz", "Nosferatu", "Metropolis", "La Passion de Jeanne d'Arc"]),
    ("Dans quel film Chaplin incarne-t-il Charlot face à une machine géante ?", "Les Temps modernes", ["Le Kid", "Les Temps modernes", "La Ruée vers l'or", "Le Cirque"]),
    ("Quel film noir de 1941 met en scène Sam Spade ?", "Le Faucon maltais", ["Le Grand Sommeil", "Le Faucon maltais", "Laura", "Assurance sur la mort"]),
    ("Quel film de Hitchcock se passe presque entièrement dans un appartement ?", "Fenêtre sur cour", ["Fenêtre sur cour", "La Main au collet", "L'Inconnu du Nord-Express", "Sueurs froides"]),
    ("Dans quel film Gene Kelly danse-t-il sous la pluie ?", "Chantons sous la pluie", ["Chantons sous la pluie", "Un Américain à Paris", "Brigadoon", "Anchors Aweigh"]),

    # --- ANNÉES 60-70 ---
    ("Quel film de 1967 met en scène Bonnie et Clyde ?", "Bonnie and Clyde", ["Bonnie and Clyde", "Badlands", "Natural Born Killers", "Butch Cassidy"]),
    ("Quel film de Stanley Kubrick est basé sur un roman d'Anthony Burgess ?", "Orange mécanique", ["Orange mécanique", "Shining", "Full Metal Jacket", "Barry Lyndon"]),
    ("Dans quel film de 1972 voit-on un cheval décapité dans un lit ?", "Le Parrain", ["Le Parrain", "Scarface", "Casino", "Il était une fois en Amérique"]),
    ("Quel film de 1975 se déroule lors d'une plongée sous-marine ?", "Les Dents de la mer", ["Les Dents de la mer", "Le Grand Bleu", "Abyss", "Piranha"]),
    ("Quel film de George Lucas a lancé la saga Star Wars ?", "Un Nouvel Espoir", ["La Menace fantôme", "Un Nouvel Espoir", "L'Empire contre-attaque", "Le Retour du Jedi"]),

    # --- ANNÉES 80 ---
    ("Quel film de 1982 met en scène un extra-terrestre abandonné sur Terre ?", "E.T.", ["E.T.", "Rencontres du troisième type", "Cocoon", "La Chose"]),
    ("Dans quel film voit-on le robot T-800 ?", "Terminator", ["RoboCop", "Terminator", "Universal Soldier", "Predator"]),
    ("Quel film de 1984 présente une école de danse dans une ville conservatrice ?", "Footloose", ["Flashdance", "Footloose", "Dirty Dancing", "Fame"]),
    ("Dans quel film de 1985 voyage-t-on avec une DeLorean ?", "Retour vers le futur", ["Knight Rider", "Retour vers le futur", "Demolition Man", "Total Recall"]),
    ("Quel film de 1986 se passe lors d'une seule journée au lycée ?", "Ferris Bueller", ["The Breakfast Club", "Ferris Bueller", "Fast Times at Ridgemont High", "Sixteen Candles"]),
    ("Quel film de Tim Burton de 1988 présente un fantôme comique ?", "Beetlejuice", ["Edward aux mains d'argent", "Beetlejuice", "Batman", "Big Eyes"]),
    ("Dans quel film de 1980 Jack Nicholson joue-t-il un écrivain fou ?", "Shining", ["Vol au-dessus d'un nid de coucou", "Shining", "The Witches of Eastwick", "Chinatown"]),
    ("Quel film de 1984 marque le retour de l'aventurier au fouet ?", "Indiana Jones et le Temple maudit", ["Les Aventuriers de l'arche perdue", "Indiana Jones et le Temple maudit", "La Dernière Croisade", "Le Royaume du crâne de cristal"]),
    ("Quel film de John Hughes réunit cinq lycéens en retenue ?", "The Breakfast Club", ["Ferris Bueller", "The Breakfast Club", "Pretty in Pink", "Seize bougies pour Sam"]),
    ("Quel film de 1987 met en scène un policier extraterrestre chasseur de primes ?", "Predator", ["Alien", "Predator", "Robocop", "Total Recall"]),

    # --- ANNÉES 90 ---
    ("Quel film de 1994 mêle gangsters, philosophie et danse ?", "Pulp Fiction", ["Pulp Fiction", "Reservoir Dogs", "True Romance", "Jackie Brown"]),
    ("Quel film d'animation Disney de 1994 met en scène un lion royal ?", "Le Roi Lion", ["Le Roi Lion", "Bambi", "Tarzan", "Pocahontas"]),
    ("Dans quel film de 1990 Kevin Costner danse avec les Sioux ?", "Danse avec les loups", ["Danse avec les loups", "Le Dernier des Mohicans", "Geronimo", "Sitting Bull"]),
    ("Quel film de 1993 présente un météorologue coincé dans une boucle temporelle ?", "Un jour sans fin", ["Un jour sans fin", "Source Code", "Edge of Tomorrow", "Looper"]),
    ("Quel film de 1994 raconte l'histoire d'un avocat atteint du sida ?", "Philadelphia", ["Philadelphia", "Dallas Buyers Club", "The Normal Heart", "Kids"]),
    ("Dans quel film de 1996 voit-on un twister géant ?", "Twister", ["The Day After Tomorrow", "Twister", "Tornado!", "Into the Storm"]),
    ("Quel film de 1997 raconte le destin d'un mathématicien de génie à Boston ?", "Will Hunting", ["Good Will Hunting", "A Beautiful Mind", "Pi", "Proof"]),
    ("Quel film de Luc Besson de 1994 met en scène un tueur à gages et une jeune fille ?", "Léon", ["Nikita", "Léon", "Le Cinquième Élément", "Taken"]),
    ("Quel film de 1999 propose une pilule rouge et une pilule bleue ?", "Matrix", ["Dark City", "Matrix", "eXistenZ", "The Thirteenth Floor"]),
    ("Dans quel film de 1998 des soldats cherchent Ryan derrière les lignes ennemies ?", "Il faut sauver le soldat Ryan", ["Il faut sauver le soldat Ryan", "La Ligne rouge", "Midway", "Stalingrad"]),

    # --- ANNÉES 2000 ---
    ("Quel film de 2001 voit Frodon quitter la Comté ?", "Le Seigneur des Anneaux : La Communauté de l'anneau", ["Le Seigneur des Anneaux : La Communauté de l'anneau", "Le Hobbit", "Eragon", "Narnia"]),
    ("Dans quel film de 2002 Spider-Man fait-il sa première apparition ?", "Spider-Man", ["The Amazing Spider-Man", "Spider-Man", "Spider-Man 2", "Spider-Man : No Way Home"]),
    ("Quel film de Miyazaki de 2001 présente une jeune fille dans un monde de bains ?", "Le Voyage de Chihiro", ["Mon Voisin Totoro", "Le Voyage de Chihiro", "Princesse Mononoké", "Nausicaä"]),
    ("Dans quel film de 2000 Russell Crowe est-il un gladiateur ?", "Gladiator", ["Ben-Hur", "Gladiator", "Troie", "Alexandre"]),
    ("Quel film de Christopher Nolan de 2000 est raconté à l'envers ?", "Memento", ["Insomnia", "Memento", "Following", "The Prestige"]),
    ("Quel film de 2003 présente Elf interprété par Will Ferrell ?", "Elf", ["Elf", "The Santa Clause", "Home Alone 3", "Jingle All the Way"]),
    ("Dans quel film de 2004 un pilote survit sur une île déserte avec un ballon ?", "Cast Away", ["The Beach", "Cast Away", "Seul au monde", "Robinson Crusoé"]),
    ("Quel film de 2006 réunit Brad Pitt et Cate Blanchett sur plusieurs continents ?", "Babel", ["Traffic", "Babel", "Syriana", "Crash"]),
    ("Dans quel film de 2008 Heath Ledger joue-t-il le Joker pour la dernière fois ?", "The Dark Knight", ["Batman Begins", "The Dark Knight", "Joker", "Batman v Superman"]),
    ("Quel film de Pixar de 2008 met en scène un robot seul sur Terre ?", "WALL-E", ["Robots", "WALL-E", "Interstellar", "A.I."]),

    # --- ANNÉES 2010 ---
    ("Quel film de 2010 présente des architectes de rêves ?", "Inception", ["Shutter Island", "Inception", "The Cell", "Source Code"]),
    ("Quel film de 2011 présente des astronautes confrontés à une force gravitationnelle bizarre ?", "Gravity", ["Gravity", "Interstellar", "Life", "The Martian"]),
    ("Dans quel film de 2013 Leonardo DiCaprio joue un courtier véreux ?", "Le Loup de Wall Street", ["Le Loup de Wall Street", "The Big Short", "Money Monster", "Wall Street"]),
    ("Quel film de 2014 présente un astronaute seul sur Mars ?", "Interstellar", ["The Martian", "Interstellar", "Gravity", "Life"]),
    ("Quel film de 2015 remporte l'Oscar du meilleur film avec un homme seul sur Mars ?", "The Martian", ["The Martian", "Gravity", "Interstellar", "Moon"]),
    ("Dans quel film de 2016 des lions marins parlent dans un parc aquatique ?", "Le Monde de Dory", ["Shark Tale", "Le Monde de Dory", "Le Monde de Nemo", "Surf's Up"]),
    ("Quel film de Damien Chazelle de 2016 présente un couple de rêveurs à Los Angeles ?", "La La Land", ["Whiplash", "La La Land", "First Man", "Babylon"]),
    ("Dans quel film de 2017 un pianiste noir joue pour des Blancs dans le sud des USA ?", "Green Book", ["Django Unchained", "Green Book", "The Help", "12 Years a Slave"]),
    ("Quel film de 2018 présente Wakanda pour la première fois ?", "Black Panther", ["Avengers: Infinity War", "Black Panther", "Captain America: Civil War", "Thor: Ragnarok"]),
    ("Quel film de 2019 remporte la Palme d'Or et l'Oscar du meilleur film ?", "Parasite", ["Once Upon a Time in Hollywood", "Parasite", "Joker", "Portrait de la jeune fille en feu"]),

    # --- ANNÉES 2020 ---
    ("Quel film de 2020 présente une pianiste noire dans le Chicago des années 20 ?", "Ma Rainey's Black Bottom", ["Ma Rainey's Black Bottom", "Judas and the Black Messiah", "One Night in Miami", "Soul"]),
    ("Dans quel film de 2021 Benedict Cumberbatch joue un cow-boy cruel ?", "The Power of the Dog", ["True Grit", "The Power of the Dog", "Brokeback Mountain", "Hostiles"]),
    ("Quel film de 2022 présente un multivers de tout à la fois ?", "Everything Everywhere All at Once", ["Doctor Strange in the Multiverse of Madness", "Everything Everywhere All at Once", "The One", "Coherence"]),
    ("Quel film de 2023 raconte l'histoire de la bombe atomique ?", "Oppenheimer", ["Dunkirk", "Oppenheimer", "Tenet", "Interstellar"]),
    ("Quel film de 2023 avec Margot Robbie brise des records au box-office ?", "Barbie", ["Barbie", "Blonde", "Birds of Prey", "Once Upon a Time in Hollywood"]),

    # --- SAGA ET UNIVERS ---
    ("Quel acteur joue Gandalf dans Le Seigneur des Anneaux ?", "Ian McKellen", ["Ian McKellen", "Christopher Lee", "Anthony Hopkins", "Derek Jacobi"]),
    ("Quel personnage de Marvel peut contrôler le tonnerre ?", "Thor", ["Thor", "Zeus", "Storm", "Red Tornado"]),
    ("Dans quelle saga trouve-t-on la planète Pandora ?", "Avatar", ["Dune", "Avatar", "Guardians of the Galaxy", "Star Trek"]),
    ("Quel film de Star Wars introduit les midi-chloriens ?", "La Menace fantôme", ["La Menace fantôme", "L'Attaque des clones", "La Revanche des Sith", "L'Empire contre-attaque"]),
    ("Dans quelle saga une alliance garde la Terre avec des robots géants ?", "Transformers", ["Pacific Rim", "Transformers", "Power Rangers", "Neon Genesis Evangelion"]),
    ("Quel acteur joue Dumbledore dans les films Harry Potter (depuis 2004) ?", "Michael Gambon", ["Richard Harris", "Michael Gambon", "Ian McKellen", "Patrick Stewart"]),
    ("Dans quel film de James Bond voit-on Goldfinger ?", "Goldfinger", ["Goldfinger", "Thunderball", "You Only Live Twice", "On Her Majesty's Secret Service"]),
    ("Quel personnage dit 'Khaaaaaan !' dans Star Trek ?", "Kirk", ["Spock", "Kirk", "McCoy", "Scotty"]),
    ("Dans quelle saga trouve-t-on les Hobbits ?", "Le Seigneur des Anneaux", ["Narnia", "Le Seigneur des Anneaux", "Harry Potter", "L'Étrange Voyage de Harold"]),
    ("Quel film DC présente la première apparition de Wonder Woman (2017) ?", "Wonder Woman", ["Batman v Superman", "Wonder Woman", "Justice League", "Aquaman"]),

    # --- OSCARS ET RÉCOMPENSES ---
    ("Quel film a remporté l'Oscar du meilleur film en 1994 ?", "Forrest Gump", ["Pulp Fiction", "Forrest Gump", "Shawshank Redemption", "Four Weddings and a Funeral"]),
    ("Quel film a remporté 11 Oscars, record partagé ?", "Titanic", ["Avatar", "Titanic", "Ben-Hur", "Lord of the Rings: Return of the King"]),
    ("Quel pays a produit Parasite, premier film non anglophone à remporter l'Oscar du meilleur film ?", "Corée du Sud", ["Japon", "Corée du Sud", "Chine", "France"]),
    ("Quelle actrice a remporté l'Oscar pour le film Monster (2003) ?", "Charlize Theron", ["Nicole Kidman", "Charlize Theron", "Hilary Swank", "Renée Zellweger"]),
    ("Quel film de 1993 a remporté l'Oscar du meilleur film ?", "Schindler's List", ["Philadelphia", "Schindler's List", "The Piano", "In the Name of the Father"]),

    # --- FILMS D'ANIMATION ---
    ("Quel est le premier long-métrage d'animation de Disney sorti en 1937 ?", "Blanche-Neige et les Sept Nains", ["Cendrillon", "Blanche-Neige et les Sept Nains", "Pinocchio", "Bambi"]),
    ("Quel film Pixar de 2001 présente des monstres qui font peur aux enfants ?", "Monstres & Cie", ["Monstres & Cie", "Monstres University", "Monsters Inc. 2", "A Bug's Life"]),
    ("Dans quel film d'animation voit-on un rat cuisinier à Paris ?", "Ratatouille", ["Ratatouille", "Bee Movie", "Gnomeo et Juliette", "The Illusionist"]),
    ("Quel film d'animation de 2010 présente des jouets abandonnés par un enfant ?", "Toy Story 3", ["Toy Story 2", "Toy Story 3", "Toy Story 4", "Small Soldiers"]),
    ("Dans quel film de Disney de 2013 la reine Elsa libère ses pouvoirs ?", "La Reine des Neiges", ["Brave", "La Reine des Neiges", "Tangled", "Wish"]),
    ("Quel film d'animation japonais de 1997 met en scène une jeune fille guerrière face à des esprits ?", "Princesse Mononoké", ["Nausicaä", "Princesse Mononoké", "Le Château dans le ciel", "Le Tombeau des lucioles"]),
    ("Dans quel film Pixar de 2009 une maison s'envole grâce à des ballons ?", "Là-haut", ["Là-haut", "WALL-E", "Brave", "Coco"]),
    ("Quel film d'animation de 2002 remporte le premier Oscar de la catégorie film d'animation ?", "Le Voyage de Chihiro", ["Shrek", "Le Voyage de Chihiro", "Ice Age", "Lilo & Stitch"]),

    # --- FILMS FRANÇAIS ---
    ("Quel film de Jean-Pierre Jeunet de 2001 met en scène une serveuse espiègle ?", "Le Fabuleux Destin d'Amélie Poulain", ["Le Fabuleux Destin d'Amélie Poulain", "Les Choristes", "Intouchables", "Le Dîner de cons"]),
    ("Dans quel film voit-on Louis de Funès en gendarme à Saint-Tropez ?", "Le Gendarme de Saint-Tropez", ["Le Corniaud", "Le Gendarme de Saint-Tropez", "La Grande Vadrouille", "L'Aile ou la Cuisse"]),
    ("Quel film de 2011 présente l'amitié entre un aristocrate paralysé et son aide-soignant ?", "Intouchables", ["Le Prénom", "Intouchables", "La Famille Bélier", "Les Émotifs anonymes"]),
    ("Qui joue Cyrano de Bergerac dans le film de 1990 ?", "Gérard Depardieu", ["Vincent Perez", "Gérard Depardieu", "Daniel Auteuil", "Jean-Paul Belmondo"]),
    ("Quel film français de 1966 met en scène un train volé par des résistants ?", "La Grande Vadrouille", ["Le Train", "La Grande Vadrouille", "Army of Shadows", "Jeux interdits"]),

    # --- HORREUR ET THRILLER ---
    ("Dans quel film de 1973 une fillette est possédée par le diable ?", "L'Exorciste", ["L'Exorciste", "Rosemary's Baby", "The Omen", "Poltergeist"]),
    ("Quel film de 1960 présente une douche fatale dans un motel ?", "Psychose", ["Psychose", "Peeping Tom", "Cape Fear", "La Corde"]),
    ("Dans quel film de 1978 Michael Myers pourchasse des lycéens ?", "Halloween", ["Halloween", "Friday the 13th", "Nightmare on Elm Street", "Scream"]),
    ("Quel film d'horreur de 1980 se passe dans un hôtel isolé sous la neige ?", "Shining", ["1408", "Shining", "The Lodge", "Misery"]),
    ("Dans quel film de 1991 un tueur mange ses victimes avec du Chianti ?", "Le Silence des agneaux", ["American Psycho", "Le Silence des agneaux", "Seven", "Copycat"]),
    ("Quel film de Jordan Peele de 2017 dénonce le racisme de manière horrifique ?", "Get Out", ["Us", "Get Out", "Nope", "Candyman"]),
    ("Dans quel film de 1984 Freddy Krueger attaque dans les rêves ?", "Les Griffes de la nuit", ["Les Griffes de la nuit", "Halloween", "Friday the 13th", "Child's Play"]),
    ("Quel film de 1996 commence par une question sur les films d'horreur ?", "Scream", ["I Know What You Did Last Summer", "Scream", "Urban Legend", "Halloween H20"]),

    # --- SCIENCE-FICTION ---
    ("Quel film de 1968 se termine par une scène choquante sur une plage avec une statue ?", "La Planète des singes", ["2001 : L'Odyssée de l'espace", "La Planète des singes", "Fahrenheit 451", "THX 1138"]),
    ("Dans quel film de Ridley Scott des androïdes cherchent leur créateur ?", "Blade Runner", ["Blade Runner", "Alien", "Prometheus", "The Martian"]),
    ("Quel film de 1985 présente une machine à voyager dans le temps faite d'une voiture ?", "Retour vers le futur", ["Timecop", "Retour vers le futur", "Time Bandits", "The Time Machine"]),
    ("Dans quel film de James Cameron des humains colonisent une planète bleue ?", "Avatar", ["Aliens", "Avatar", "The Abyss", "Titanic"]),
    ("Quel film de 2014 explore des trous de ver pour sauver l'humanité ?", "Interstellar", ["Gravity", "Interstellar", "The Martian", "Elysium"]),
    ("Quel film de 1977 présente R2-D2 et C-3PO pour la première fois ?", "Star Wars : Un Nouvel Espoir", ["Star Wars : La Menace fantôme", "Star Wars : Un Nouvel Espoir", "Star Wars : L'Empire contre-attaque", "Rogue One"]),
    ("Dans quel film de Denis Villeneuve des humains apprennent la langue alien ?", "Premier Contact", ["Premier Contact", "Annihilation", "Rencontres du troisième type", "Contact"]),

    # --- WESTERNS ---
    ("Quel film de Sergio Leone présente l'Homme sans nom ?", "Le Bon, la Brute et le Truand", ["Il était une fois dans l'Ouest", "Le Bon, la Brute et le Truand", "Pour une poignée de dollars", "Et pour quelques dollars de plus"]),
    ("Quel acteur incarne John Wayne dans de nombreux westerns ?", "John Wayne", ["Clint Eastwood", "John Wayne", "Henry Fonda", "James Stewart"]),
    ("Quel film de John Sturges est un remake des Sept Samouraïs ?", "Les Sept Mercenaires", ["Les Sept Mercenaires", "Rio Bravo", "High Noon", "The Magnificent Seven"]),
    ("Quel western de 1969 met en scène Butch Cassidy ?", "Butch Cassidy et le Kid", ["Tombstone", "Butch Cassidy et le Kid", "Pat Garrett and Billy the Kid", "Jesse James"]),
    ("Dans quel film de Tarantino Django retrouve sa femme dans le sud esclavagiste ?", "Django Unchained", ["Inglourious Basterds", "Django Unchained", "The Hateful Eight", "Jackie Brown"]),

    # --- COMÉDIES ---
    ("Dans quel film de 1959 Billy Wilder deux musiciens fuient la mafia déguisés en femmes ?", "Certains l'aiment chaud", ["Certains l'aiment chaud", "The Apartment", "Avanti!", "Kiss Me, Stupid"]),
    ("Quel film de 1994 présente un détective animalier excentrique ?", "Ace Ventura", ["Ace Ventura", "The Mask", "Dumb and Dumber", "Liar Liar"]),
    ("Dans quel film de 1980 une parodie de film catastrophe présente des avions et du plastique ?", "Y a-t-il un pilote dans l'avion ?", ["Top Secret!", "Y a-t-il un pilote dans l'avion ?", "Hot Shots!", "Les Nuls : L'Film"]),
    ("Quel film de Woody Allen de 1977 remporte l'Oscar du meilleur film ?", "Annie Hall", ["Manhattan", "Annie Hall", "Hannah et ses sœurs", "Stardust Memories"]),
    ("Dans quel film de 2004 des lycéennes forment des clans sociaux impitoyables ?", "Mean Girls", ["Clueless", "Mean Girls", "She's All That", "Bring It On"]),

    # --- DRAMES ---
    ("Quel film de Frank Darabont de 1994 se passe dans une prison du Maine ?", "Les Évadés", ["Le Jeu de la mort", "Les Évadés", "The Green Mile", "Dead Man Walking"]),
    ("Dans quel film de 1957 Henry Fonda doit convaincre 11 jurés ?", "Douze Hommes en colère", ["Douze Hommes en colère", "To Kill a Mockingbird", "Witness for the Prosecution", "Anatomy of a Murder"]),
    ("Quel film de 1995 présente un avocat courageux qui défend un homme noir dans le sud ?", "À cause d'un meurtre", ["Philadelphia", "À cause d'un meurtre", "Sleepers", "Ghosts of Mississippi"]),
    ("Dans quel film de 2013 Solomon Northup est vendu comme esclave ?", "12 Years a Slave", ["Django Unchained", "12 Years a Slave", "Roots", "Lincoln"]),
    ("Quel film de 2015 présente l'enquête du Boston Globe sur les abus de l'Église ?", "Spotlight", ["Spotlight", "All the President's Men", "The Post", "Frost/Nixon"]),

    # --- FILMS MUSICAUX ---
    ("Dans quel film de 1965 Julie Andrews joue une gouvernante qui chante ?", "La Mélodie du bonheur", ["Mary Poppins", "La Mélodie du bonheur", "Camelot", "My Fair Lady"]),
    ("Quel film de 1978 met en scène John Travolta et Olivia Newton-John dans un lycée ?", "Grease", ["Saturday Night Fever", "Grease", "Fame", "Rock Around the Clock"]),
    ("Dans quel film musical de 2001 Nicole Kidman joue dans un cabaret parisien ?", "Moulin Rouge!", ["Chicago", "Moulin Rouge!", "Nine", "Cabaret"]),
    ("Quel film de 2002 présente Renée Zellweger en meurtrière qui veut devenir star ?", "Chicago", ["Cabaret", "Chicago", "Nine", "Moulin Rouge!"]),
    ("Dans quel film d'animation de 2016 des animaux chantent dans un concours ?", "Sing", ["Zootopia", "Sing", "The Lorax", "Minions"]),

    # --- BOX-OFFICE ET RECORDS ---
    ("Quel film détient le record mondial du box-office en 2023 ?", "Avatar : La Voie de l'eau", ["Avengers: Endgame", "Avatar : La Voie de l'eau", "Top Gun: Maverick", "The Lion King 2019"]),
    ("Quel film de Spielberg de 1993 a révolutionné les effets spéciaux avec des dinosaures ?", "Jurassic Park", ["The Lost World", "Jurassic Park", "Jurassic World", "Land Before Time"]),
    ("Quel acteur a joué dans le plus grand nombre de films Marvel ?", "Samuel L. Jackson", ["Robert Downey Jr.", "Samuel L. Jackson", "Chris Evans", "Scarlett Johansson"]),
    ("Quel est le film d'horreur le plus rentable de tous les temps (proportionnellement) ?", "L'Exorciste", ["Paranormal Activity", "L'Exorciste", "Halloween", "Blair Witch Project"]),
    ("Quel film de 2022 est sorti à la fois au cinéma et a sauvé les salles post-Covid ?", "Top Gun: Maverick", ["Doctor Strange 2", "Top Gun: Maverick", "Thor: Love and Thunder", "The Batman"]),

    # --- ANECDOTES ET CURIOSITÉS ---
    ("Quel film de 1994 a failli avoir Johnny Depp dans le rôle principal avant Tom Hanks ?", "Forrest Gump", ["Cast Away", "Forrest Gump", "Philadelphia", "The Green Mile"]),
    ("Quel acteur a refusé le rôle de Neo dans Matrix ?", "Will Smith", ["Brad Pitt", "Will Smith", "Nicolas Cage", "Tom Cruise"]),
    ("Quel film présente pour la première fois un effet de zoom avant/arrière dit 'Dolly zoom' ?", "Les Dents de la mer", ["Vertigo", "Les Dents de la mer", "Raging Bull", "Goodfellas"]),
    ("Dans quel film de 1974 Mel Brooks parodie-t-il le western ?", "Blazing Saddles", ["Young Frankenstein", "Blazing Saddles", "Silent Movie", "High Anxiety"]),
    ("Quel film de 1941 est souvent considéré comme le plus grand film de tous les temps ?", "Citizen Kane", ["Casablanca", "Citizen Kane", "Rules of the Game", "Sunset Boulevard"]),
]

# ✅ Insérer exactement 200 questions
for i, q in enumerate(questions[:200]):
    Question.objects.create(
        text=q[0],
        option1=q[2][0],
        option2=q[2][1],
        option3=q[2][2],
        option4=q[2][3],
        correct_answer=q[1]
    )

print(f"✅ {Question.objects.count()} questions cinéma ajoutées avec succès !")