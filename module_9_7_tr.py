# def is_prime(func):
#     def true_prime(*args, **kwargs):
#         number = func(*args, **kwargs)
#         if number > 2:
#             for number in range(2, int(number ** 0.5) + 1):
#                 if number % number == 0:
#                     print("Составное")
#                 else:
#                     print("Простое")
#         return number
#     return true_prime()
def is_prime(func):
    def true_prime(*args, **kwargs):
        number = func(*args, **kwargs)
        if number < 2:
            return False
        for i in range(number, int(number ** 0.5) + 1):
            if number % i == 0:
               return False
            print("Простое")
            #return True
        # if is_prime(number):
        #     print("Простое")
        # else:
        #     print("Составное")
        else:
            print("Составное")
        return number
    return true_prime


@is_prime
def sum_three(*args):
    total = 0
    for num in args:
        total += num
    return total

# def sum_three(*args):
#
#     return sum(args)
result = sum_three(2, 3, 6)

print(result)

#