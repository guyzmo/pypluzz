Python Pluzz Interface
----------------------

Pluzz is the national french television video on demand platform.
This program downloads movies, and gets metadata of movies.

    Pluzz Downloader

    Downloads a movie from the French Television VOD

    Usage:
    pluzz_downloader.py gui [<id>] [-t <target>] [--avconv <avconv>] [--verbose]
    pluzz_downloader.py fetch <id> [-t <target>] [--avconv <avconv>] [--verbose]
    pluzz_downloader.py get <id> [<key>]
    pluzz_downloader.py show <id>
    pluzz_downloader.py list [<category>] [<channel>] [-l <limit>] [-s <sort>] [-i]
    pluzz_downloader.py search <query> [<category>] [<channel>] [-l <limit>] [-s <sort>] [-i]

    Commands:
    gui                    Launch graphical user interface.
    get                    Get list of keys.
    get <key>              Get value for key.
    show                   Give summary for key.
    fetch                  Download the TV show.
    list                   List TV shows.
    search <query>         Search a TV show.

    Options for `list` and `search` commands:
    <query>                Terms of the show to look up.
    <category>             Category to list. `help` or no value gives the list.
    <channel>              Channels to list. `help` or no value gives the list.
    -l --limit <limit>     Number of shows to output. [default: 100]
    -s --sort <sort>       Sort the output (alpha, date, relevance) [default: alpha]
    -i --image             Show thumbnail image URL for the show

    Options for `get`, `show` and `fetch` commands:
    <id>                   URL or ID of the TV show
    -t --target <target>   Target directory to download the file to [default: ~/Downloads]
    --avconv <avconv>      Sets full path to avconv binary [default: /usr/bin/avconv]
    -V --verbose           Show more output.
    -h --help              Show this screen.

    (c)2014 Bernard `Guyzmo` Pratz
    Under the WTFPL <http://wtfpl.net>


 * Forewords

The Pluzz name is certainly a registred trademark from *France Televisions*. All I hope
is that they will be open minded enough to let us *borrow* the Pluzz name for this program,
and leave us the legal ability to download programs from Pluzz, which is the only way to
access programs using only opensource software.

Example
-------

     % bin/pypluzz list seriefiction france4
    101973830 -- Archer                                  
    101973959 -- Band of Brothers : l'enfer du Pacifique 
    101973960 -- Band of Brothers : l'enfer du Pacifique 
    101973962 -- Black Mirror                            
    101973873 -- Crapuleuses                             
    101973825 -- Doctor Who                              
    101973826 -- Doctor Who                              
    101973827 -- Doctor Who                              
    101973821 -- Les aventures du jeune Indiana Jones    
    101973828 -- Monster                                 
    101973829 -- Monster                                 
    101507110 -- Un gars, une fille                      
    101777131 -- Un gars, une fille                      
    101777132 -- Un gars, une fille                      
    101787192 -- Un gars, une fille                      
    101973871 -- Un gars, une fille                      
    102037331 -- Un gars, une fille                      
    102037333 -- Un gars, une fille                      
    102037334 -- Un gars, une fille                      
    102037907 -- Un gars, une fille                      
    102037909 -- Un gars, une fille                      
    102037910 -- Un gars, une fille                      
    101973929 -- Un gars, une fille                      
    102041448 -- Un gars, une fille                      
    102041449 -- Un gars, une fille                      
     % bin/pypluzz show 101973825
    Summary of the show 'Doctor Who'
            id: 101973825                       id AEDRA: F42095445291228620141005      
    Broadcast: On 10 May 2014 at 20:45           Length: 00:45:00                      
        Genre: Série fantastique                 Season: 7                             
    Website: http://www.france4.fr/emissions/doctor-who
        Pluzz: http://pluzz.francetv.fr/videos/doctor_who_,101973825.html
    Channel: France 4                         Picture: /staticftv/ref_emissions/2014-05-10/EMI_437155_214.jpg
        Rights: CSA1                          
        Crew:
                    Acteur: Rigg, Diana
                Réalisateur: Metzstein, Saul
                Scénariste: Gatiss, Mark
                    Acteur: Stirling, Rachael
                    Acteur: McIntosh, Neve
                    Acteur: Smith, Matt
                    Acteur: Stewart, Catrin
                    Acteur: Starkey, Dan
                    Acteur: Coleman, Jenna-Louise
                    Acteur: de Leon Allen, Eve
    Synopsis:
        En 1893, des cadavres, qui tous ont une peau d'une inquiétante
    couleur rouge, sont découverts dans un canal. Une Silurienne, madame
    Vastra, enquête sur le phénomène avec son épouse humaine, Jenny, et
    leur majordome, Strax. Ils découvrent, en examinant l'oeil d'une
    victime, que la dernière chose qu'elle a vue est le Docteur. Cela les
    pousse à se rendre dans le Yorkshire, où se trouve la communauté
    dirigée par madame Gillyflower et le mystérieux monsieur Sweet. En
    s'infiltrant dans les bâtiments, Jenny retrouve le Docteur, enchaîné
    et dont la peau est devenue rouge comme celle des morts du canal...
     % bin/pypluzz fetch 101973825
    Download and convert: [##################################################################################                                    ] 69% ETA: 23s/33s
    Download and convertion done: 'Downloads/doctor_who_101973825.mkv' saved


Screenshot
----------

UI for looking up a show:

![UI](http://m0g.net/stuff/pypluzz-list.png)

UI for downloading a show:

![UI](http://m0g.net/stuff/pypluzz-show.png)

Resources
---------

originally posted as a gist on:

 * https://gist.github.com/guyzmo/3b18193d6bea07bac37c

designed as an answer for that question:

 * http://stackoverflow.com/questions/23562651

and discussed over there:

 * http://forum.ubuntu-fr.org/viewtopic.php?pid=16869701#p16869701

as a fork of:

 * http://doc.ubuntu-fr.org/tutoriel/pluzz.fr


