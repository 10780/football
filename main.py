teams_confeds = {'USA':'CONCACAF', 'Mexico':'CONCACAF', 'Russia':'UEFA', 'England':'UEFA',
                        'Brazil':'CONMEBOL', 'Korea DPR':'AFC', 'Australia':'AFC', 'South Africa':'CAF',
                        'Liberia':'CAF', 'Argentina':'CONMEBOL', 'Fiji':'OFC'}

#sepcific function for looking up keys by values (teams by confederation)
def values_search(dict, values):
    keys = []
    values_list = dict.items() #use this for values search
    for item in values_list: #look up and add to list
        if item[1] == values:
            keys.append(item[0])
    return keys

def search():
    repeat = True #validation loop (user has try again option)
    while repeat == True:
        usr_select = input("Enter a country or confederation (type either 'country' or 'confederation': ")
        if usr_select == 'country' or usr_select == 'Country' or usr_select =='COUNTRY':
            #set search flag
            country_search = True
            confed_search = False
        elif usr_select == 'confederation' or usr_select == 'Confederation' or usr_select == 'CONFEDERATION':
            #set search flag
            confed_search = True
            country_search = False
        else:
            #program exits on error
            print("Error, exiting program")
            repeat = False
        #search countries
        while country_search == True:
            usr_search = input("\nEnter name of country: ")
            if usr_search in teams_confeds:
                print("\n", usr_search, "search result:")
                print('{} is in {} Confederation'.format(usr_search, teams_confeds[usr_search]))
                #change flags to false to end program
                country_search = False
                repeat = False
            else:
                print("Nothing found")
                try_again = input("Try again? (y/n)")
                if try_again == 'y' or try_again == 'Y':
                    repeat = True
                elif try_again == 'n' or try_again == 'N':
                    print("Ok")
                    country_search = False
                    repeat = False
                else:
                    #program exits on error
                    print("Error, exiting program")
                    country_search = False
                    repeat = False
        #search confederations (this was the harder one and does not work exactly like country search)
        while confed_search == True:
            usr_search = input("\nEnter name of confederation: ")
            keys = values_search(teams_confeds, usr_search)
            print("\n", usr_search, "search result:")
            #iterate through list from values_search function
            for i, team in enumerate(keys):
                print('{} Confederation includes {}'.format(usr_search, team))
                if team in keys:
                    confed_search = False
                    repeat = False
                else:
                    print("Nothing found")
                    try_again = input("Try again? (y/n)")
                    if try_again == 'y' or try_again == 'Y':
                        repeat = True
                    elif try_again == 'n' or try_again == 'N':
                        print("Ok")
                        confed_search = False
                        repeat = False
                    else:
                        #program exits on error
                        print("Error, exiting program")
                        confed_search = False
                        repeat = False
        
search()
