import sublime
import sublime_plugin

class DiscardOtherTabsCommand(sublime_plugin.WindowCommand):
    def run(self, all_windows=False, group=None, index=None):
        # Determine which windows to operate on:
        # - Default: current window only.
        # - If all_windows is True, close tabs in every window.
        # The target tab to keep is identified using (group, index) from the tab
        # context menu, or defaults to the active view if not provided.
        windows = [self.window] if not all_windows else sublime.windows()
        for win in windows:
            # Default to the active view unless group/index are specified
            target_view = (
                win.views_in_group(group)[index]
                if group is not None and index is not None
                else win.active_view()
            )
            # Copy the list of views to avoid issues when closing tabs.
            for view in win.views():
                # Leave the target view open.
                if view != target_view:
                    # Mark as scratch to discard changes.
                    view.set_scratch(True)
                    view.close()
