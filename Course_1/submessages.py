def submessages(s):
  if len(s) == 0:
    return {""}
  last = s[-1]
  without_last = s[:-1]
  result = submessages(without_last)
  for m in list(result):
    result.add(m + last)
  return result

if __name__ == "__main__":
# should print {"", "a", "b", "aa", "ab", "ba", "aba"}
# elements of the set can be printed in a different order
    print(submessages("aba"))