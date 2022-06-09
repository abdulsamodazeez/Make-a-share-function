#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: abdulsamod

"""


def Make_a_share(sentence):
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
print(f"case 1: {Make_a_share('Am I allowed to share your email')}")

print(f"case 2: {Make_a_share('May I share your email')}")

print(f"case 3: {Make_a_share('can i share your email')}")

print(f"case 4: {Make_a_share('i want to share your email')}")

print(f"""case 5: {Make_a_share("Will you help my friends if I share your email with them?")}""")
     
print(f"case 6: {Make_a_share('I am able share your email')}")

print(f"case 7: {Make_a_share('I shall share your email')}")

print(f"case 8: {Make_a_share('I already shared the email')}")

print(f"case 9: {Make_a_share('I shall share')}")

print(f"case 10: {Make_a_share('should i email')}")


