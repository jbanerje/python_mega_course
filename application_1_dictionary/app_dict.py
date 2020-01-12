import json
from difflib import get_close_matches

def find_meaning_from_dict(word):
    ''' Function to call the word meaning from dictionary'''

    if word in data :
        return (data[word])
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0 :
        word1 = input('Did you mean %s instead (y/n)?' % get_close_matches(word, data.keys())[0])
        if word1 == 'y':
           new_word = get_close_matches(word, data.keys())[0] 
           return (data[new_word])
        else:
            return('Thank You for using dictionary!')

    else:
        return('Word not available in dictionary!')


# Main Function
if __name__ == "__main__":
    data = json.load(open('application_1_dictionary/data.json'))
    word = input ('Enter a word:')
    comment = find_meaning_from_dict(word.lower())
    print(comment)

    