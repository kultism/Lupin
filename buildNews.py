import json
import urllib
import requests

newslist = {}
newslist['news'] = []
newslist['news'].append({
    'newsid': 1,
    'date': '2020-02-11',
    'news': 'Verion 2.0.0 alpha updates\nLupin now supports Time Spaced Repetition based on SM2 algorithm!!\n Import your flashcards directly \
from your github by running /tsr import ... you can then go over your pending flashcards using /tsr x where \
x is the number of cards you\'d like to see. If you don\'t specify x the value set in your config.ini will be used.\
\nAlso Lupin can now pull these news updates after each significatif update. This will keep you posted about the latest news.\n\n \
This version requires new values in your config.ini file'
})

newslist['news'].append({
    'newsid': 2,
    'date': '2020-02-15',
    'news': 'Verion 3.0.0 experimental updates\n \
A new version upgrade introducing MinMap capabilties among other thing. \
Send /getMM pageTitle and Lupin will generate a Markmap file containing a mindmap of that page and send it to you. \nCredits to https://markmap.js.org/\n \
/tsr command is now renamed to /srs'
})

newslist['news'].append({
    'newsid': 3,
    'date': '2020-02-18',
    'news': 'Verion 3.1.0 experimental updates\n \
Thanks to @Piotr 3 months calendar can now be autogenerated and inserted in your right side-bar. Version releases also a new command /pullnow that forces refresh from GitHub & a scheduled pull that can be configured from the config.ini `GitHubUpdateFrequency` \
\n\nVersion requires new values in your config.ini file, please reffer to config.sample.ini'
})

newslist['news'].append({
    'newsid': 4,
    'date': '2020-02-20',
    'news': 'Verion 3.2.0 & 3.3.0 experimental updates\n \
Timestamps in Journal entries can now be turned off from the config.ini file by setting `timestampEntries = false` \
TODOCommand is now decomissioned and replaced by CommandsMap for greater flexibility. Mapp your own sets of commands like \
TODO LATER etc...\n\n Version requires modifications in your config.ini file, please reffer to config.sample.ini'
})

newslist['news'].append({
    'newsid': 5,
    'date': '2020-02-26',
    'news': 'Verion 3.4.0 experimental updates\n \
With all the great themes why have only one? put your choice of themes in the /logseq directory and name them ThemeName.custom.css\
then simply call Lupin with /themes to switch between one and the other.'
})

newslist['news'].append({
    'newsid': 6,
    'date': '2020-03-02',
    'news': 'Verion 3.5.0 alpha updates\n \
Added feature to control how many months (0 to 3) you want LUPIN to generate calendars for, this is controlled thru generateMonths array of config.ini.\
first [0|1] specifies if you want LUPIN to generate prev month, second [0|1] specifies if you want LUPIN to generate next month\
1,1 will generate prev,cur,next | 0,1 will generate curr,next | 0,0 will only generate curr'
})

newslist['news'].append({
    'newsid': 7,
    'date': '2020-03-22',
    'news': 'Verion 3.8.0 experimental updates\n \
Lupin now supports doker thanks to Jon Molina https://github.com/digitalknk.\
Lupin also now supports Twitter embedding, Send a twitter URL to Lupin and see what happens.'
})

with open('news.json', 'w') as outfile:
    json.dump(newslist, outfile)
