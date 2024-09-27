import re

pattern = r'\d+'
text = "Tengo 2 gatos y 3 perros"
matches = re.findall(pattern, text)
print(matches)