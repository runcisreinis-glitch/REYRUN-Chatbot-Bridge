# Publishing the static site

Run `python3 publishing/render.py` from a checked-out copy to generate the three
home pages, README files, skill references and download archive. Stage the
contents of `web/` as your static root and copy the repository's `launchers/`
directory to `/launchers/` within that root. Keep all the files when deploying
to an HTTPS site. The browser file check uses Web Crypto.

Run `python3 scripts/build_launchers.py` after changing a launcher source.
Run the checks in `tests/` against their stated operating systems before
publishing updated assets. The GitHub workflow uses fresh user fixtures.
