# -*- coding: utf-8 -*-
"""
    Jellybeans Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class JellybeansStyle(Style):

    background_color = '#151515'
    styles = {
        Token:              '#e8e8d3 bg:#151515',
        Generic.Emph:       '#c000c0 underline',
        Name.Constant:      '#ff00ff underline',
        Generic.Deleted:    '#40000A bg:#700009 bold',
        Name.Variable:      '#008b8b underline',
        String:             '#99ad6a',
        Keyword.Type:       '#2e8b57 bold underline',
        Generic.Inserted:   '#D2EBBE bg:#437019 bold',
        Name.Tag:           '#a52a2a bold',
        Keyword:            '#a52a2a bold',
        Comment.Preproc:    '#a020f0 underline',
        Name.Entity:        '#6a5acd bold',
        Generic.Error:      '#ffffff bg:#ff0000',
        Comment:            '#8a2be2 bold',
        Name.Attribute:     '#fad07a',
        Name.Function:      '#fad07a',
        Generic.Traceback:  'bg:#902020',
        Generic.Subheading: '#70b950 bold',
        Generic.Heading:    '#70b950 bold',
        Generic.Output:     '#606060 bold',
    }
