# FirstPrintCheck: first-printer data

Spec table for 10 beginner 3D printers, one row per printer: enclosure, build volume, footprint, nozzle, bed, ABS capability, multicolor, noise and local (offline) printing. In `first-printers.csv` every spec column is paired with a `*_source` column holding the maker page it was read from. In `first-printers.json` each cell is an object with the value, the source URL (`src`) and the exact phrase on that page (`quote`); `null` means the figure is not on the maker page.

Source and latest version: https://firstprintcheck.com/tools/first-printer-picker/

How the data was gathered: maker product pages and manuals, each cell cites its URL; cells with no published figure are left blank. From the data file: "Every non-empty spec cell carries the maker page it came from (src) and the exact phrase on that page (quote)."

License: CC BY 4.0 - credit FirstPrintCheck and link to the page.

Cite as: FirstPrintCheck. First-printer data. https://firstprintcheck.com/tools/first-printer-picker/. Retrieved 2026-10-24.

Embed the live table:

```html
<iframe src="https://firstprintcheck.com/tools/first-printer-picker/embed/" width="100%" height="600" loading="lazy" title="FirstPrintCheck first printer picker"></iframe>
```

Last checked: 2026-10-24
