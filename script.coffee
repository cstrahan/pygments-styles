$ ->
  downloadThemes = (cb) ->
    $.getJSON("themes.json").done(cb)

  downloadStyle = (style, cb) ->
    $.ajax({'url': "/themes/#{style}.css", 'cache': true}).done (css) ->
      cb(css.replace(/\.highlight/g, ".highlight.theme-#{style}"))

  styles = ["bw", "emacs"]
  theme = $("link#theme")

  downloadThemes (styles) ->
    $.Mustache.load('code.mustache').done ->
      # populate code samples
      pygments_styles = _.where(styles, {'source': 'pygments'})
      vim_styles = _.where(styles, {'source': 'vim'})

      $('#container').mustache 'code',
        "styles": pygments_styles

      $('#container').mustache 'code',
        "styles": vim_styles
        "foo": "bar"

      $('#container').masonry
        'itemSelector': '.item',
        'isAnimated':   !Modernizr.csstransitions,

      # fetch css
      for style in styles
        do (style)->
          downloadStyle style.name, (css) ->
            stylesheet = $('<style></style>')
            stylesheet.text(css)
            $("head").append(stylesheet)
