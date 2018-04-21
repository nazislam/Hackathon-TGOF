if __name__ == '__main__':
    file = open("map.txt", "r")
    lines = []
    for line in file:
        lines.append(line)
    file.close()
    x = 19
    y = 1
    while x >= 0:
        lines[x] = lines[x][:y - 1] + "*" + lines[x][y:]
        y += 1
        lines[x] = lines[x][:y - 1] + "*" + lines[x][y:]
        y += 1
        x -= 1
    y = 40
    x = 0
    while x <= 60:
        lines[x] = lines[x][:y - 1] + "*" + lines[x][y:]
        x += 1
        lines[x] = lines[x][:y - 1] + "*" + lines[x][y:]
        x += 1
        lines[x] = lines[x][:y - 1] + "*" + lines[x][y:]
        x += 1
        y -= 1
    file = open("map1.txt", "w")
    for line in lines:
        file.write(line)
        file.write("\n")

