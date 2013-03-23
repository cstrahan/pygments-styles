# -*- coding: utf-8 -*-
"""
    Candy Colorscheme
    ~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class CandyStyle(Style):

    background_color = '#000000'
    styles = {
        Token:              '#f0f0f8 bg:#000000',
        Name.Constant:      '#90d0ff underline',
        Generic.Deleted:    '#a0d0ff bg:#0020a0 bold',
        Name.Variable:      '#40f0f0 bold underline',
        Generic.Traceback:  '#ffa0ff bg:#c00000 bold',
        Keyword.Type:       '#ffc864 underline',
        Generic.Inserted:   '#a0d0ff bg:#0020a0 bold',
        Name.Tag:           '#ffa0ff bold',
        Keyword:            '#ffa0ff bold',
        Comment.Preproc:    '#40f0a0 underline',
        Name.Entity:        '#e0e080 bold',
        Generic.Error:      '#ffffff bg:#ff6060 bold',
        Comment:            '#c0c0d0 bold',
        Generic.Subheading: '#f0f0f8 bold',
        Generic.Heading:    '#f0f0f8 bold',
        Generic.Output:     '#4080ff bold',
        Generic.Emph:       'underline',
    }
