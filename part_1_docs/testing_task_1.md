### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  
  # There is no constructor here

  def check_for_ace(self, card):
  # This should be the equality operator instead of assignment
    if card.value = 1:
      return True
    # else needs a colon after it
    else 
      return False
   
  # This should be def instead of dif. A comma is needed between function arguments
  dif highest_card(self, card1 card2):
  # This code block should be indented because it is the function code 
  if card1.value > card2.value:
    # This should return card1, we have not passed card into the function so it will not know what it is
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # total needs to be assigned a value (0)
  total 
  for card in cards:
    total += card.value
    # The return statement needs to be outside of the for loop, or the loop will only run once then return.
    return "You have a total of" + total
  

```

