# -*- coding: utf-8 -*-
"""
    Stackoverflow Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class StackoverflowStyle(Style):

    background_color = '#eeeeee'
    styles = {
            Token:              '#000000',
            Number:             '#800000',
            Comment:            '#808080',
            String:             '#800000',
            String.Symbol:      '#800000',
            Name.Constant:      '#2b91af',
            Keyword.Type:       '#2b91af',
            Generic.Inserted:   '#000000',
            Keyword:            '#00008b',
            Generic.Error:      '#000000',
            Generic.Output:     '#000000',
            Name.Variable:      '#000000',
            Name.Tag:           '#000000',
            Name.Entity:        '#000000',
            Comment.Preproc:    '#808080',
            Generic.Heading:    '#000000',
            Generic.Emph:       'underline',
            Name.Function:      '#000000',
            Generic.Subheading: '#000000',
            Number.Float:       '#800000',
            Name.Attribute:     '#000000',
            Name.Label:         '#000000',
            Name.Other:         '#000000',
            Generic.Deleted:    '#000000',
            Operator.Word:      '#000000',
            }
