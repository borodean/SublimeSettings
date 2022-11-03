import sublime
import sublime_plugin

delim = ' '

class SortWordsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    sel = view.sel()
    for region in sel:
      content = view.substr(region)
      newContent = delim.join(sorted(content.split(delim)))
      view.replace(edit, region, newContent)
