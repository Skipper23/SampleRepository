"""
Assignment 3.
"""
import datetime

def main():
    """
    This scripts will ask to enter user personal information and collect the
    following pieces of date from the use.
    """
    name = str(input('Please enter your Name: ')) # return the user type name
    gender = str(input('Please enter your Gender (Male/Female/none-binary): ')) # return the user type gender
    birthplace = str(input('Please enter your Birthplace: ')) # return the user type birthplace

    try:
        birthdate = (input('Please enter your Birthdate in YYYY-MM-DD: ')) # return the user type birthdate
        sinNumber = int(input('Please enter your Social Insurance number: ')) # return the user type SIN number

    except ValueError:
        print('Error: Please enter in numbers') ## this line will raise an error if you input strings or letters

# Gender function
    def Gender():
        """
        This function will check and returned the given gender output
        """
        var_male = 'male. He was'
        var_female = 'female. She was'
        var_none = 'non-binary. They were'

        if gender == 'm' or gender == 'M': # check if it's a male
            return var_male
        elif gender == 'male' or gender == 'Male':
            return var_male
        elif gender == 'f' or gender == 'F': # check if it's female
            return var_female
        elif gender == 'female' or gender == 'Female':
            return var_female
        else: # check if it's a non binary
            return var_none

# Age function
    def Age():
        """
        This functions will calculate the user age based on today's date
        """
        var_birthdate = birthdate # birthdate is input variable from main() functions
        var_datetime = datetime.datetime.strptime(var_birthdate, '%Y-%m-%d') # datetime format
        birthyear = var_datetime.year # isolating the user type birth year
        today = datetime.datetime.today() # current date time
        current_year = today.year # isolating the year output from today variable
        age = int(current_year) - int(birthyear) # subtracting the current year and birth year
        return age

# ProNoun function
    def ProNoun():
        """
        This function use a gender specific pronouns based on the
        output given Gender() functions
        """
        n_male = 'his'
        n_female = 'her'
        n_none = 'their'

        if gender == 'm' or gender == 'M': # check if it's a male
            return n_male
        elif gender == 'male' or gender == 'Male':
            return n_male
        elif gender == 'f' or gender == 'F': # check if it's a female
            return n_female
        elif gender == 'female' or gender == 'Female':
            return n_female
        else:
            return n_none # check if it's a non-binary

    # Print output information
    print(f'"{name} is {Age()} a year old {Gender()} born in {birthplace} and {ProNoun()} SIN # is {sinNumber}"') # output user information

# Do not edit below
if __name__ == '__main__':
    main()
