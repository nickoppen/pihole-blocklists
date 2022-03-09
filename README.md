# pihole-blocklists

A basic list of social media and messaging sites for use with the pi-hole ad-blocking software. Download and use locally or add to your ad-lists using the permalink in the top of the file.

To add a file to your Adlist append the file name above to https://nickoppen.github.io/pihole-blocklists/ e.g. https://nickoppen.github.io/pihole-blocklists/vpn-surfshark.com.txt

Domains can change quickly so the lists will soon be out of date. Test after loading!

For more see: https://github.com/crpietschmann/pi-hole-blocklist and https://github.com/gieljnssns/Social-media-Blocklists

If you have additions, please add a pull request or just add an Issue.

Some sites have hundreds of sub-domains so are better suited to a wildcard blacklist (e.g. (\.|^)deviantart$). However, if there are lots of subdomains and you want to list them all individually, you can use SecurityTrails.com. Free accounts are available for infrequent users and I've include a short python script to automatically create a blocklist from a given domain.
