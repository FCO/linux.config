config.load_autoconfig(False)
c.fonts.hints = "30pt"
c.fonts.prompts = "30pt"
c.fonts.statusbar = "25pt"
c.fonts.completion.entry = "25pt"
c.fonts.completion.category = "25pt"
c.fonts.messages.info = "25pt"
c.fonts.messages.warning = "25pt"
c.fonts.messages.error = "25pt"




# Usa o backend que realmente funciona no Raspberry Pi
c.backend = "webkit"

# Reduz latência de renderização
# c.web.private_browsing = False
# c.web.prefetch = True

# Desativa suavização pesada do WebKit
c.scrolling.smooth = False

# Aceleração opcional (não é perfeita no WebKit, mas ajuda)
c.qt.args += ["--enable-accelerated-2d-canvas"]
c.qt.args += ["--ignore-gpu-blocklist"]
# Melhor pipeline de vídeo e HTML5
c.content.autoplay = False
# c.content.javascript_can_open_windows_automatically = False

# Mantém o WebKit mais leve
c.content.cookies.accept = "never"
c.content.plugins = False

# Reduz uso de memória
c.completion.height = "25%"
c.completion.shrink = True
c.completion.scrollbar.padding = 0
c.completion.scrollbar.width = 6

