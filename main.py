name = input("რა გქვია? ")
lastName = input("რა გვარის ხარ? ")
year = input("რამდენი წლის ხარ? ")
answer = ""
#String ანუ str() არის სიტყვები 
#INtegers ანუ int() არის ციფრები


# git add . ვამატებ ფაილებს
# git commit -m "აქ დავწერ კომენტარს ჩემ ცვლილებებზე"
# git push ჩემ ცვლილებებს ავტვირთავ
# git push --set-upstream origin ბრენჩის სახელი დაწერე ეს იმისთვის არის როდესაც ქმნი ახალ ვერსიას ანუ ბრენჩს

print(f"გამარჯობა {name} {lastName} \t")
if int(year) < 18:
    answer = "მაპატიე ზედმეტად ახალგაზრდა ხარ"
else:
    answer = "რამხელა ყოფილხარ ბიჭოოოოოო"
print(answer)