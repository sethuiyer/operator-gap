# The Operator Gap

An interactive mathematical journey from decimal permutations to the Weil positivity criterion and the missing global construction.

## Read

Open `index.html` directly, or run `python3 -m http.server 8000` and visit http://localhost:8000. The page embeds its JavaScript, fonts, and artwork and includes eight interactive D3 explanations and a 24-source bibliography. Supporting documents linked from the article are included alongside it.

## Reproduce

- `python3 mighty_k_audit.py` runs the standard-library exact arithmetic checks and regenerates `mighty_k_exact_results.json`.
- `python3 -m pip install -r requirements.txt`, then `python3 scripts/numerical_bump.py` reproduces the smooth-test numerical example using NumPy and SciPy. Its quadrature results are estimates, not interval-certified bounds.

`mighty_k_weil_audit.md` contains the detailed project audit. `MILESTONE_A.md` develops the prime-adapted extension. These are project research notes; the article distinguishes them from classical results. No proof of RH is claimed.

## Editing

`index.html` is the current, authoritative article. Its styles and scripts are embedded, including D3 and KaTeX. Original illustration assets are in `blog_assets/`.

Third-party libraries and embedded fonts retain their respective licenses; this repository does not relicense those dependencies.
