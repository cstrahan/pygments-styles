# -*- coding: utf-8 -*-
"""
    Guardian Colorscheme
    ~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class GuardianStyle(Style):

    background_color = '#332211'
    styles = {
        Token:              '#ffffff bg:#332211',
        Operator.Word:      '#cc9966 bg:#008080 bold',
        Generic.Deleted:    '#ffffff bg:#884444 bold',
        Name.Label:         '#ffccff bg:#000000 bold',
        Number:             '#bbddff bg:#c00000 bold',
        Name.Attribute:     '#ffddaa bg:#000000 bold',
        Comment:            '#dddddd bg:#334455 bold',
        Generic.Emph:       '#ff6060 bg:#000000 underline',
        Name.Constant:      '#ffffff bg:#808080 bold underline',
        Keyword.Type:       '#ff7788 bg:#000000 bold underline',
        Number.Float:       '#bbddff bg:#c00000 bold',
        Generic.Inserted:   '#ffffff bg:#446688 bold',
        Keyword:            '#ffffcc bg:#000000 bold',
        Generic.Error:      '#ffffff bg:#8080ff bold',
        Generic.Output:     '#ffeecc bg:#808080 bold',
        Generic.Subheading: '#ffffff bg:#c00000 bold',
        Name.Variable:      '#8080ff bg:#000000 bold underline',
        Generic.Traceback:  '#ff0000 bg:#000000 bold',
        Name.Function:      '#ffddaa bg:#000000 bold',
        Name.Exception:     '#66ffcc bg:#000000 bold',
        Name.Tag:           '#ffffcc bg:#000000 bold',
        String:             '#ffffcc bg:#000000 italic',
        Generic.Heading:    '#ffffff bg:#c00000 bold',
        Name.Entity:        '#bbddff bg:#c00000 bold',
        Comment.Preproc:    '#ffcc99 bg:#0000c0 bold underline',
    }
