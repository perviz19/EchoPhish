file_path = 'output/ip_agent.log'

# Dosyayı okuma modunda aç
with open(file_path, 'r') as file:
    lines = file.readlines()

last_line = lines[-1:]

user_agent =  last_line[0].split(": ", 1)[1]
print(user_agent)