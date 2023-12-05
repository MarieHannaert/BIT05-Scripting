#!/usr/bin/python3
item=input("geef een stirng die je wilt splitten:")
letters=len(item)
character=input('geef character:')
def split_sort_join(item,character)
gesplitst=item.split(character)
print("testen voor gesplitst {} --> {}".format(item,gesplitst))
gesplitst.sort()
print("is the list sorted? {}".format(gesplitst))
list_join=character.join(gesplitst)
print("joined bach togheter {}".format(list_join))
    