# Publishing the static site

Run `python3 publishing/render.py` from a checked-out copy to generate the three
home pages, README files, skill references and download archive. Stage the
contents of `web/` as your static root and copy the repository's `launchers/`
directory to `/launchers/` within that root. Keep all the files when deploying
to an HTTPS site. The browser file check uses Web Crypto.

Run `python3 scripts/build_launchers.py` after changing a launcher source.
Run the checks in `tests/` against their stated operating systems before
publishing updated assets. The GitHub workflow uses fresh user fixtures.

The file checker has a static address in each language, including its share metadata. To update the social artwork after editing the bridge illustration, run `python3 publishing/make-share-images.py` with a Playwright browser installed, then deploy the generated JPEGs with the site.

The two Windows XML launchers use PowerShell bundled in the CMD. They only manage the fixed Latvian translation file. The installer accepts the two plug-in hashes listed in `scripts/rdr2/install-xml.ps1`. See `research/xml-installer.json` for the observed scope. To run the Windows fixture, pass a folder containing copies of the two known plug-ins and the verified XML to `tests/xml-install-restore.ps1`. The fixture creates fresh game folders under the temporary directory.
