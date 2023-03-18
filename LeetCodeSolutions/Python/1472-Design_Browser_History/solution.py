# https: // leetcode.com/problems/design-browser-history/submissions/917744904/

# Runtime: 217 ms, faster than 86.55% of Python3 online submissions for Design Browser History.
# Memory Usage: 16.7 MB, less than 70.51% of Python3 online submissions  for Design Browser History.
#
# Problem:
#   You have a browser of one tab where you start on the homepage and you 
#   can visit another url, get back in the history number of steps or move 
#   forward in the history number of steps.

#   Implement the BrowserHistory class:
#      BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#      void visit(string url) Visits url from the current page. It clears up all the forward history.
#      string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
#      string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class BrowserHistory:

    def __init__(self, homepage: str):
        self.pageIndex = 0
        self.links = [homepage]

    def visit(self, url: str) -> None:
        self.links = self.links[:self.pageIndex+1]
        self.links.append(url)
        self.pageIndex += 1

    def back(self, steps: int) -> str:
        if (self.pageIndex-steps >= 0):
            self.pageIndex -= steps
        else:
            self.pageIndex = 0
        return self.links[self.pageIndex]

    def forward(self, steps: int) -> str:
        if (self.pageIndex + steps < len(self.links)):
            self.pageIndex += steps
        else:
            self.pageIndex = len(self.links) - 1
        return self.links[self.pageIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
