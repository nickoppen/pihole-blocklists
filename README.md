# pihole-blocklists

Lists of social media, messaging and now gaming sites for use with the [pi-hole](https://pi-hole.net) ad-blocking software. I believe that the lists will also work with [AdguardHome](https://github.com/AdguardTeam/AdGuardHome) and [Blocky](https://github.com/0xERR0R/blocky).

The gaming sites are a very blunt instrument. They will probably block most if not all games by that publisher. Use the white list if you want to block most and leave a few open. 

To add a file to a pi-hole Adlist add the file name above to the address: https://nickoppen.github.io/pihole-blocklists/. I'm not sure how to link to ad lists for other blockers.

For more see: https://github.com/crpietschmann/pi-hole-blocklist,  https://github.com/gieljnssns/Social-media-Blocklists and Steven Blacks excellent [hosts](https://github.com/StevenBlack/hosts) project.

If you have additions, please add a pull request or just add an Issue.

Some sites have hundreds of sub-domains so are better suited to a wildcard blacklist (e.g. (\.|^)reddit$). 

However, if there are lots of subdomains and you want to list them all individually, you can use SecurityTrails.com. Free accounts are available for infrequent users and I've included a short python script (getSubdomains.py) to automatically create a blocklist from a given domain.

See also: [phishing.army](https://phishing.army/)
