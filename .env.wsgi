# The Kodi webserver only supports HTTP.
# Uncomment KODI_SCHEME to tell the skill to use https between AWS/Heroku and your local network
# (only use if you have already set this up with your own certificates)
#
# KODI_SCHEME=https

# If using a reverse proxy you might need to add an extra bit to the url before "jsonrpc"
# You can do this with KODI_SUBPATH (don't use slashes before or after)
#
# KODI_SUBPATH=

KODI_ADDRESS=
KODI_PORT=
KODI_USERNAME=
KODI_PASSWORD=

# If you want to enable WOL, set these variables.
# If your skill endpoint is on the same subnet as the kodi host, only set the mac
# and the magic packet will be sent to the broadcast address.  If you set a port,
# then it assumes that the endpoint is not local and wake-on-wan is required.
# In this case the magic packet is sent to KODI_ADDRESS:KODI_WOL_PORT, and your
# router will need to be set up to forward this on appropriately.
KODI_WOL_MAC =
KODI_WOL_PORT =

SKILL_APPID=
SKILL_VERIFY_CERT=

# Your local time zone for responses that include absolute times.
# See https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
#
# For example, if you are in the Eastern US time zone, you would use:
# SKILL_TZ=US/Eastern
#
# Leave empty or undefined (commented out) if you don't need or want absolute
# time responses.  An example is asking when the currently playing item will
# end.  If you have SKILL_TZ defined, it will also tell you the wall-clock
# time when the item will conclude.
SKILL_TZ=
