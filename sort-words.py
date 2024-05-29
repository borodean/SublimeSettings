import sublime_plugin

class SortWordsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    sel = view.sel()
    for region in sel:
      content = view.substr(region)
      view.replace(edit, region, sort_words(content))

def detect_separator(input: str):
  for separator in [", ", "; ", " "]:
    if separator in input:
      return separator
  raise ValueError("No valid separator found in the input.")

def sort_words(input: str):
  separator = detect_separator(input)
  words = input.split(separator)
  sorted_words = sorted(words)
  return separator.join(sorted_words)
