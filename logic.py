def feedback(code, guess):
    exact = 0
    used_code = [False] * len(code)
    used_guess = [False] * len(guess)

    # First pass: exact matches
    for i, (a, b) in enumerate(zip(code, guess)):
        if a == b:
            exact += 1
            used_code[i] = True
            used_guess[i] = True

    # Second pass: partial matches
    partial = 0
    for i, ch in enumerate(guess):
        if used_guess[i]:
            continue

        for j, code_ch in enumerate(code):
            if not used_code[j] and ch == code_ch:
                partial += 1
                used_code[j] = True
                break

    return exact, partial
