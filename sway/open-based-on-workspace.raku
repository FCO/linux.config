#!/usr/bin/env raku
use Sway::API;

my $sway = Sway::API.new;

multi MAIN("open") {
   given $sway.current-workspace<num> {
      when 1  { shell "foot &"     }
      when 2  { shell "chromium &" }
      default { shell "foot &"     }
   }
}

