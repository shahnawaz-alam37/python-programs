def divide (x, y):
    try:
        result = x//y
        print ("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print ("Sorry ! You are dividing by zero ")
    except ValueError:
        print ("Invalid value")
    except TypeError:
        print ("different datatype")
divide (3, 'g')
