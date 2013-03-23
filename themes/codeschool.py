# -*- coding: utf-8 -*-
"""
    Codeschool Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class CodeschoolStyle(Style):

    background_color = '#252c31'
    styles = {
        Token:              '#f0f0f0 bg:#252c31',
        Number:             '#3c98d9',
        Comment:            '#9a9a9a italic',
        Generic.Output:     '#414e58 bg:#232c31 bold',
        String:             '#8bb664',
        Comment.Preproc:    '#dda790',
        Name.Entity:        '#f0f0f0',
        Generic.Heading:    '#f0f0f0 bold',
        Name.Tag:           '#dda790',
        Name.Function:      '#bcdbff',
        Name.Variable:      '#99cf50',
        Generic.Subheading: '#f0f0f0 bold',
        Keyword:            '#dda790',
        Generic.Inserted:   'bold',
        Number.Float:       '#3c98d9',
        Keyword.Type:       '#b5d8f6',
        Name.Constant:      '#3c98d9',
        Generic.Emph:       'underline',
        Name.Attribute:     '#bcdbff',
        Name.Label:         '#8bb664',
        Generic.Deleted:    '#880708 bold',
        Operator.Word:      '#dda790',
    }
