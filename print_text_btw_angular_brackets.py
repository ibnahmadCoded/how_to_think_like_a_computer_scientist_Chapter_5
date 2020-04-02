text = "abnke <http://alegeaa.com> jkdm"

openb_pos = text.find("<")

closeb_pos = text.find(">", openb_pos)

tx = text[openb_pos+1:closeb_pos]

print(tx)
