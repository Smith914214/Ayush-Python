  # Nested dictionary

student = {
    "name" : "anish",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 99
    }
}

print(student["subject"]["chem"])