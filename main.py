def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  # print(text)
  word_count = get_word_count(text)
  letter_count = get_letter_count(text)

  get_report(book_path,word_count, letter_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  amount_of_words = len(text.split())
  return amount_of_words
  
def get_letter_count(text):
  diction= {}
  text_lowered = text.lower()
  for letter in text_lowered:
    if letter in diction:
      diction[letter] += 1
    else:
      diction[letter] = 1
  return diction

def get_report(book_path,word_count, letter_count):
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  letter_count_list = []
  for letter in letter_count:
    letter_count_list.append({"name":letter,"num":letter_count[letter]})
  letter_count_list.sort(reverse=True, key=sort_on)
  for item in letter_count_list:
    print(f"The '{item['name']}' character was found {item['num']} times")
  print("--- End report ---")

def sort_on(dict):
  return dict["num"]


main()