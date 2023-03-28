def key_error(code):
    subjects = {
        "ab101": "Computability and complexity",
        "ab102": "Software engineering",
        "ab103": "Database systems basics",
        "ab104": "Applied Information Systems",
        "ab105": "Data transfer basics" }
    return subjects[code]

print(key_error("ab101"))
print(key_error("cd105"))