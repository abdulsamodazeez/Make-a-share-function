#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: abdulsamod

"""


def text_filter(sentence):
    key_word_1= "share"
    key_word_2= "email"
    sentence= sentence.lower()
    
    if key_word_1.lower() not in sentence:
        pass
    elif key_word_2.lower() not in sentence:
        pass
    elif any([sentence.startswith("may"), sentence.startswith("will"),
            sentence.startswith("should"), sentence.startswith("can"),
            sentence.startswith("shall"), sentence.startswith("could"),
            sentence.startswith("am"), sentence.startswith("would")]) or "want" in sentence:
                return "Student wants to know if can share"
    else:
            return "Student has shared"
        
       
      #TESTING
print(f"case 1: {text_filter('Am I allowed to share your email')}")

print(f"case 2: {text_filter('May I share your email')}")

print(f"case 3: {text_filter('can i share your email')}")

print(f"case 4: {text_filter('i want to share your email')}")

print(f"""case 5: {text_filter("Will you help my friends if I share your email with them?")}""")
     
print(f"case 6: {text_filter('I am able share your email')}")

print(f"case 7: {text_filter('I shall share your email')}")

print(f"case 8: {text_filter('I already shared the email')}")

print(f"case 9: {text_filter('I shall share')}")

print(f"case 10: {text_filter('should i email')}")


