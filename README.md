# pihole-blocklists

A basic list of social media and messaging sites for use with the [pi-hole](https://pi-hole.net) ad-blocking software. I believe that the lists will also work with [AdguardHome](https://github.com/AdguardTeam/AdGuardHome) and [Blocky](https://github.com/0xERR0R/blocky).

To add a file to a pi-hole Adlist append the file name above to https://nickoppen.github.io/pihole-blocklists/ e.g. https://nickoppen.github.io/pihole-blocklists/vpn-surfshark.com.txt I'm not sure how to link to ad lists for other blockers.

For more see: https://github.com/crpietschmann/pi-hole-blocklist and https://github.com/gieljnssns/Social-media-Blocklists

If you have additions, please add a pull request or just add an Issue.

Some sites have hundreds of sub-domains so are better suited to a wildcard blacklist (e.g. (\.|^)reddit$). 

However, if there are lots of subdomains and you want to list them all individually, you can use SecurityTrails.com. Free accounts are available for infrequent users and I've include a short python script (getSubdomains.py) to automatically create a blocklist from a given domain.
