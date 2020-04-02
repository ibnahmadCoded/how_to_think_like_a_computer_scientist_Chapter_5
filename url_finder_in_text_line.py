text = "abnke http://alegeaa.com jkdm"

url_pos = text.find("http://")

space_pos = text.find(" ", url_pos)

url = text[url_pos:space_pos]

print(url)
