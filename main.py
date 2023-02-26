

import Variables

from Logins import login
from Cooking_Facts_Generator import cooking_facts_generator


def main():
   login_success = login(Variables.username, Variables.password)

   if login_success:
        print("YouTube login was successful")
   else:
       print("YouTube login was not successful")





if __name__ == '__main__':
    main()
