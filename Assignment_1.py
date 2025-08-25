# Header with name, assignment, and class

print("Jennifer Dang")
print("Assignment 1")
print("IS826: Application Programming\n")

# Assigned the title of assignment as a string (%SCIENTIFIC DISCOVERIES OF 2016%) to a variable (title_1)

title_1 = "%SCIENTIFIC DISCOVERIES OF 2016%\n"

# Centers the title 80 characters wide
print(title_1.center(80))

# First Header and Section
# Added indentation to mimic assignment layout for both header and sections
# Used triple quotation for setting string that spans across multiple lines

print("""Discovery 1: "New Prime Number Discovered"
    Mathematicians discovered a new prime number in January via the Great
    Internet Mersenne Prime Search. The new prime number is 2^74,207,281 -
    1.\n
    You might be asking why there is a project to determine such a number.
    Modern cryptography requires the use of Mersenne Prime numbers (Of
    which only 49 have been discovered) and other complex numbers to encode
    data. The new prime number is currently the record holder for the
    longest prime and is almost 5 million digits longer than its
    predecessor. The total number of digits in the new prime falls just
    under 24,000,000 making '2^74,207,281 - 1' the only practical way to
    write it.\n""")
      
# Second Header and Section
# Added indentation to mimic assignment layout for both header and sections
# Used triple quotation to set up string that spans across multiple lines

print("""Discovery 2: "Nearly Eternal Data Storage Method Discovered"
    Everything degrades eventually, and there is no way to store data on one
    device for truly extended periods of time. But that may no longer
    be true due to a discovery made by the University of Southampton.
    Scientists have successfully used nano-structured glass to create a
    process for recording and retrieving data. The storage device is a
    small glass disk about the size of an American quarter that can hold
    360TB of data and remain intact up to 1,000°C. This means that its
    average shelf life when held at room temperature would be approximately
    13.8 billion years (Roughly the same amount of time the universe has
    existed).""")
