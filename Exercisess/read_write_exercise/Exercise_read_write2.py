with open("E:/Programming/Crash Course of Python by Google/Exercisess/read_write_exercise/stocks.csv","r") as f, open("E:/Programming/Crash Course of Python by Google/Exercisess/read_write_exercise/output.csv","w") as out:
    out.write("Company Name, PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock=tokens[0]
        price=float(tokens[1])
        eps=float(tokens[2])
        book=float(tokens[3])
        pe=round(price/eps,2)
        pd=round(price/book,2)
        out.write(f"{stock},{pe},{pd}\n")

