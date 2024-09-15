def link2mdlink(link, repr_link):
    # [Duck Duck Go](https: // duckduckgo.com)
    return "[{repr_link}]({link})".format(repr_link=repr_link, link=link)
