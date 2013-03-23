# -*- coding: utf-8 -*-
"""
    Railscasts Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class RailscastsStyle(Style):

    background_color = '#232323'
    styles = {
        Token:              '#E6E1DC bg:#232323',
        Name.Constant:      '#6D9CBD underline',
        Generic.Deleted:    '#E6E1DC bg:#008080 bold',
        Name.Variable:      '#CFCFFF bold underline',
        Generic.Traceback:  '#ffffff bg:#ff0000',
        String:             '#A5C160',
        Generic.Inserted:   '#E6E1DC bg:#144212 bold',
        Name.Tag:           '#CC7733 bold',
        Keyword:            '#CC7733 bold',
        Comment.Preproc:    '#ff80ff underline',
        Name.Entity:        '#ff4500 bold',
        Generic.Error:      '#FFFFFF bg:#ff6060',
        Comment:            '#BC9357 bold italic',
        Name.Attribute:     '#FFC66D',
        Keyword.Type:       'underline',
        Name.Function:      '#FFC66D',
        Generic.Subheading: '#E6E1DC bold',
        Generic.Heading:    '#E6E1DC bold',
        Generic.Emph:       'underline',
        Generic.Output:     '#8a2be2 bold',
    }
