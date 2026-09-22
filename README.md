# MAVP project page

Static project website for **MAVP: Map-Aware Visuomotor Policies for Mobile Manipulation**. The page follows the structure of the [AutoIntervene project page](https://aus.bot/research/autointervene/): a paper overview, six individual task demos, and experimental results displayed as HTML tables and charts.

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
- `assets/images/`: web exports of standalone artwork from the Overleaf source (`figure1_tasks.png` and `mavp_overview_release.pdf`). No paper-page screenshots are used.
- `assets/paper/MAVP.pdf`: the current eight-page Overleaf PDF supplied on 22 September 2026.

The experimental results are semantic HTML tables and CSS/JavaScript charts using the numbers in the paper. The policy-family chart reads Table V directly from the page, so its values stay in sync with the table.

The public demos were reviewed for people in frame. Existing privacy-masked masters were used for five tasks; the Conveyor Picking edit starts after an unmasked operator leaves the frame. The Dual-Drawer Return source was reviewed separately and contains no visible person.

The `scripts/` tools can regenerate the six web videos from local originals and export the source figures from a local copy of the Overleaf project. Those source inputs are outside this public repository.
