def verify_card_number(string):
    card_number = [num for num in string if num.isdigit()]
    double_every_second = []
    if len(card_number) % 2 == 1:
        for i in range (len(card_number)):
            if i % 2 == 0:
                double_every_second.append(int(card_number[i]))
            elif i % 2 == 1:
                the_number = card_number[i] * 2
                while len(str(the_number)) != 1:
                    the_number = sum([int(num) for num in str(the_number)])
                double_every_second.append(int(the_number))
    else:
        for i in range (len(card_number)):
                    if i % 2 == 1:
                        double_every_second.append(int(card_number[i]))
                    elif i % 2 == 0:
                        the_number = card_number[i] * 2
                        while len(str(the_number)) != 1:
                            the_number = sum([int(num) for num in str(the_number)])
                        double_every_second.append(int(the_number))

    SUM = sum(double_every_second)
    if SUM % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number("453914881"))
print(verify_card_number("453914889"))
print(verify_card_number("4111-1111-1111-1111"))
print(verify_card_number("1234 5678 9012 3456"))