Python Pluzz Interface
----------------------

Pluzz is the national french television video on demand platform.
This program downloads movies, and gets metadata of movies.

    Usage:
        pluzz_downloader.py [<url>] pull [-t <target>] [--avconv <avconv>]
        pluzz_downloader.py <url> get [<key>]
        pluzz_downloader.py <url> show
        pluzz_downloader.py gui

    Commands:
        gui                    Launch graphical user interface
        get                    Get list of keys
        get <key>              Get value for key
        show                   Give summary for key

    Options:
        -t --target <target>   Target directory to download the file to [default: ~/Downloads]
        --avconv <avconv>      Sets full path to avconv binary [default: /usr/bin/avconv]
        -h --help              Show this screen.
        --version              Show version.

(c)2014 Bernard `Guyzmo` Pratz
Under the WTFPL <http://wtfpl.net>

Screenshot
----------

![UI](http://m0g.net/stuff/pypluzz.png)

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


