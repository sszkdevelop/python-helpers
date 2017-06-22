"""
Sriharsha Samala
"""

class DateProcessor(object):
    """
    processes date things
    """
    def __init__(self):
        self = self
        self.month_abbrs = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        self.month_proper = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.extradate_words = ['present', 'now', 'current', 'date', 'cont', 'continued']

    def ismonth(self, tok):
        """
        return bool if string is a month
        """
        for m in self.month_abbrs:
            if tok.lower().startswith(m):
                return True
        return False

    def getmonth(self, tok):
        """
        return proper name for abbreviated month
        """
        for m_pos in range(0, len(self.month_abbrs)):
            if tok.lower().startswith(self.month_abbrs[m_pos]):
                return self.month_proper[m_pos]
        return "not a month"

    def getmonth_byidx(self, idx):
        """
        return month given proper number
        """
        return self.month_proper[idx-1]

    def getmonthpos(self, mon):
        for m in range(0, len(self.month_abbrs)):
            if self.month_abbrs[m] == mon:
                return m+1
        for m in range(0, len(self.month_proper)):
            if self.month_proper[m] == mon:
                return m+1
        return 0

    def isyear(self, num):
        """
        check if number is a reasonable year
        """
        if num < 100:
            if num < 25 or num > 80:
                return True
        elif num < 2025:
            if num > 1980:
                return True
        return False

    def getyear(self, num):
        """
        format double digit year to 4-digit
        """
        if num < 100:
            if num < 25:
                return 2000 + num
            if num > 80:
                return 1900 + num
        return num

    def isextraword(self, term):
        """
        if string is non-time that describes the date, return true
        """
        for n in self.extradate_words:
            if term.lower() == n:
                return True
        return False
