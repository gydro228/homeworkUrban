def generate_password(n):
    password = ''
    pairs = []

    for i in range(1, 21):
        if i == n:
            continue
        for j in range(1, 21):
            if j == n or j == i:
                continue
            pairs.append((i, j))

    for (i, j) in pairs:
        pair_sum = i + j
        if n % pair_sum == 0:
            password += f"{i}{j}"

    return password

for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")
