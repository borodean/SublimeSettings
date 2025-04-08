import sublime
import sublime_plugin

class DiscardOtherTabsCommand(sublime_plugin.WindowCommand):
    def run(self, all_windows=False):
        # Determine which windows to operate on:
        # - Default: current window only.
        # - If all_windows is True, close tabs in every window.
        windows = [self.window] if not all_windows else sublime.windows()
        for win in windows:
            active_view = win.active_view()
            # Copy the list of views to avoid issues when closing tabs.
            for view in win.views():
                # Leave the active (currently focused) view open.
                if view != active_view:
                    # Mark as scratch to discard changes.
                    view.set_scratch(True)
                    view.close()
