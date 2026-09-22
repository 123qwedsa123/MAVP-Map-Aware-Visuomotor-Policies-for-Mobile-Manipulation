# MAVP project page

Static project website for **MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation**. The page follows the structure of the [AutoIntervene project page](https://aus.bot/research/autointervene/): a paper overview, six individual task demos, and figures and tables cropped from the MAVP paper.

## Preview

From this directory:

```sh
python3 -m http.server 8765
```

Open <http://127.0.0.1:8765/>.

## Publish with GitHub Pages

This repository is a static site; no build step is needed. In the GitHub repository, open **Settings → Pages**, choose **Deploy from a branch**, and select **main** and **/(root)**. The project URL will be:

<https://123qwedsa123.github.io/MAVP-Map-Aware-Visuomotor-Policies-for-Mobile-Manipulation/>

## Media

- `assets/videos/`: six compressed H.264/AAC task demos with the original instrumental MAVP soundtrack. Each video is separate and can be played on the page.
- `assets/posters/`: video preview frames.
- `assets/images/`: unedited figure and table crops from the current MAVP paper draft. These are screenshots, not a public copy of the LaTeX source or manuscript PDF.

The public demos were reviewed for people in frame. Existing privacy-masked masters were used for five tasks; the Conveyor Picking edit starts after an unmasked operator leaves the frame. The Dual-Drawer Return source was reviewed separately and contains no visible person.

The `scripts/` tools can regenerate the media from the local paper PDF and local original video assets. Those inputs are deliberately outside this public repository.
