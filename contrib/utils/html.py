import re

def convert_1252_codes(text):
    """Convert windows-1252 characters to appropriate html entities.
    
    @param str String to filter
    @type string/unicode
    @return unicode version of filtered string
    
    Adapted from: http://effbot.org/zone/unicode-gremlins.htm
    
    """
    cp_1252_chars = {
        # from http://www.microsoft.com/typography/unicode/1252.htm
        u"\x80": u"&#8364;", # EURO SIGN
        u"\x82": u"&#8218;", # SINGLE LOW-9 QUOTATION MARK
        u"\x83": u"&#402;",  # LATIN SMALL LETTER F WITH HOOK
        u"\x84": u"&#8222;", # DOUBLE LOW-9 QUOTATION MARK
        u"\x85": u"&#8230;", # HORIZONTAL ELLIPSIS
        u"\x86": u"&#8224;", # DAGGER
        u"\x87": u"&#8225;", # DOUBLE DAGGER
        u"\x88": u"&#710;",  # MODIFIER LETTER CIRCUMFLEX ACCENT
        u"\x89": u"&#8240;", # PER MILLE SIGN
        u"\x8A": u"&#352;",  # LATIN CAPITAL LETTER S WITH CARON
        u"\x8B": u"&#8249;", # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
        u"\x8C": u"&#338;",  # LATIN CAPITAL LIGATURE OE
        u"\x8E": u"&#381;",  # LATIN CAPITAL LETTER Z WITH CARON
        u"\x91": u"&#8216;", # LEFT SINGLE QUOTATION MARK
        u"\x92": u"&#8217;", # RIGHT SINGLE QUOTATION MARK
        u"\x93": u"&#8220;", # LEFT DOUBLE QUOTATION MARK
        u"\x94": u"&#8221;", # RIGHT DOUBLE QUOTATION MARK
        u"\x95": u"&#8226;", # BULLET
        u"\x96": u"&#8211;", # EN DASH
        u"\x97": u"&#8212;", # EM DASH
        u"\x98": u"&#732;",  # SMALL TILDE
        u"\x99": u"&#8482;", # TRADE MARK SIGN
        u"\x9A": u"&#353;",  # LATIN SMALL LETTER S WITH CARON
        u"\x9B": u"&#8250;", # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
        u"\x9C": u"&#339;",  # LATIN SMALL LIGATURE OE
        u"\x9E": u"&#382;",  # LATIN SMALL LETTER Z WITH CARON
        u"\x9F": u"&#376;",  # LATIN CAPITAL LETTER Y WITH DIAERESIS
    }

    if re.search(u"[\x80-\x9f]", text):
        def fixup(m):
            s = m.group(0)
            return cp_1252_chars.get(s, s)
        if isinstance(text, type("")):
            text = unicode(text, "iso-8859-1")
        text = re.sub(u"[\x80-\x9f]", fixup, text)
        
    return unicode(text)