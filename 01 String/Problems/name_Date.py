# Write a program fill in a letter template given below with the name and date

letter = '''
            Dear <|Name|>
            You are Selected.
            <|Date|>
'''

print(letter.replace("<|Name|>", "Kunal").replace("<|Date|>", "23 Dec 2025"))