# # print("Victor Nara")

# fullname = "Victor Nara"
# age = 100
# married = False
# hobbies = ['football', 'singing', 'dancing']
# kids = {
#     "paul": "male",
#     "maurice": "male",
#     "ama":"female"
# }

# # print(hobbies)

# # if statement
# if (married == True):
#     print("Happy marriage")
# else:
#     print("Save the date!")


# # function definition
# def sayHello():
#     print("Hello World")

# let score = 0;
# let num = 3;

# while (true) {
# 	if (num % 3 === 0) {
# 		let a = prompt("Please input a multiple");
# 		score += num;
# 		num = parseInt(a);
# 	} else {
# 		alert("Game over, your score: " + score);
# 		break;
# 	}
# }

def is_a_multiple(number, multiple):
    """
      Returns true if a given number is a multiple of another number,
      otherwise return false.

      @param: number   -> int (number to check)
      @param: multiple -> int (number/multiple to check against)
      """
    if (number % multiple == 0):
        return True
    else:
        return False


def game_of_multiples(number):
    score = 0
    num = 3

    while (True):
        if (num % 3 == 0):
            response = input("Please input a multiple")
            score = score + num
            num = int(response)
        else:
            print("Game over, your score: " + str(score))
            break


def fullname(first, last):
    return first + " " + last

# print(fullname("victor", "nara"))
# arr = [100,15,45,90,"Gone", False]
# fname = "Victor Nara"


def reverser(data):
    # empty variable to hold reversed data
    rev = ""
    neg = -1

    while (len(rev) != len(data)):
        rev = rev + data[neg]
        neg = neg + -1

    return rev

# print(reverser("Tom Sawyer"))
