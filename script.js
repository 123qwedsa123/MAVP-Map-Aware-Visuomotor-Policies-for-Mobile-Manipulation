const videos = [...document.querySelectorAll("video")];

for (const video of videos) {
  video.addEventListener("play", () => {
    for (const other of videos) {
      if (other !== video && !other.paused) other.pause();
    }
  });
}

const policyTable = document.getElementById("policy-table");
const policyVisual = document.getElementById("policy-visual");
const policyChart = document.getElementById("policy-chart");
const familyButtons = [...document.querySelectorAll("[data-family]")];

if (policyTable && policyVisual && policyChart && familyButtons.length) {
  const rows = [...policyTable.tBodies[0].rows].map((row) => {
    const values = [...row.cells].slice(1).map((cell) => Number.parseInt(cell.textContent, 10));
    return {
      task: row.cells[0].textContent.trim(),
      ACT: values.slice(0, 2),
      DP: values.slice(2, 4),
      FM: values.slice(4, 6),
    };
  });

  const render = (family) => {
    const fragment = document.createDocumentFragment();

    for (const row of rows) {
      const chartRow = document.createElement("div");
      chartRow.className = "chart-row";

      const task = document.createElement("div");
      task.className = "chart-task";
      task.textContent = row.task;

      const pair = document.createElement("div");
      pair.className = "chart-pair";

      row[family].forEach((value, index) => {
        const series = document.createElement("div");
        series.className = "chart-series";
        series.setAttribute("aria-label", `${row.task}: ${index === 0 ? "unanchored velocity" : "map-frame pose"}, ${value}% success`);

        const track = document.createElement("span");
        track.className = "bar-track";
        const bar = document.createElement("span");
        bar.className = `bar-fill ${index === 0 ? "velocity" : "pose"}`;
        bar.style.width = `${value}%`;
        track.append(bar);

        const number = document.createElement("strong");
        number.textContent = `${value}%`;
        series.append(track, number);
        pair.append(series);
      });

      chartRow.append(task, pair);
      fragment.append(chartRow);
    }

    policyChart.replaceChildren(fragment);
    for (const button of familyButtons) {
      button.setAttribute("aria-pressed", String(button.dataset.family === family));
    }
    policyVisual.hidden = false;
  };

  for (const button of familyButtons) {
    button.addEventListener("click", () => render(button.dataset.family));
  }

  render("ACT");
}

const copyCitation = document.getElementById("copy-citation");
const bibtex = document.getElementById("bibtex");
const citationStatus = document.getElementById("citation-status");

if (copyCitation && bibtex && citationStatus) {
  copyCitation.hidden = false;
  copyCitation.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(bibtex.textContent.trim());
      citationStatus.textContent = "BibTeX copied to clipboard.";
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(bibtex);
      selection?.removeAllRanges();
      selection?.addRange(range);
      citationStatus.textContent = "Automatic copy is unavailable. Select the BibTeX above and copy it manually.";
    }
  });
}
