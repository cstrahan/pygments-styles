# -*- coding: utf-8 -*-
"""
    Vividchalk Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class VividchalkStyle(Style):

    background_color = '#000000'
    styles = {
        Token:              '#EEEEEE bg:#000000',
        Name.Constant:      '#339999 underline',
        Generic.Deleted:    '#8a2be2 bg:#008080 bold',
        Name.Variable:      '#FFCC00 underline',
        String:             '#66FF00',
        Keyword.Type:       '#AAAA77 underline',
        Name.Tag:           '#FF6600 bold',
        Keyword:            '#FF6600 bold',
        Comment.Preproc:    '#AAFFFF underline',
        Name.Entity:        '#33AA00 bold',
        Generic.Error:      '#ffffff bg:#ff0000',
        Comment:            '#9933CC bold italic',
        Generic.Inserted:   'bg:#00008b bold',
        Generic.Traceback:  'bg:#ff0000',
        Generic.Subheading: '#ff00ff bold',
        Generic.Heading:    '#ff00ff bold',
        Generic.Output:     '#404040 bold',
        Generic.Emph:       'underline',
    }
