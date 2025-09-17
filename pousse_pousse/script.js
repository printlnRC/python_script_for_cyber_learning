const container = document.getElementById('puzzle-container');
const tiles = [];
let emptyPosition = { row: 3, col: 3 };
let puzzleSignature = ''; 

console.log("╔═╗┬ ┬┌┐ ┌─┐┬─┐   ╦  ┌─┐┌─┐┬─┐┌┐┌┬┌┐┌┌─┐ ┌─┐┬─┐");
console.log("║  └┬┘├┴┐├┤ ├┬┘───║  ├┤ ├─┤├┬┘││││││││ ┬ ├┤ ├┬┘");
console.log("╚═╝ ┴ └─┘└─┘┴└─   ╩═╝└─┘┴ ┴┴└─┘└┘┴┘└┘└─┘o└  ┴└─");
console.log("67 121 98 101 114 45 76 101 97 114 110 105 110 103 46 102 114 ");

fetch('init_puzzle.php')
  .then(response => response.json())
  .then(data => {
    const { positions, labels, signature } = data;
    puzzleSignature = signature; 

    for (let i = 0; i < 16; i++) {
      if (positions[i] === 15) {
        emptyPosition.row = Math.floor(i / 4);
        emptyPosition.col = i % 4;
        continue;
      }


      const tileIndex = positions[i];
      const imageRow = Math.floor(tileIndex / 4);
      const imageCol = tileIndex % 4;

      const tile = document.createElement('div');
      tile.classList.add('tile');

      tile.style.backgroundPosition = `-${imageCol * 100}px -${imageRow * 100}px`;

      const row = Math.floor(i / 4);
      const col = i % 4;

      tile.style.gridRowStart = row + 1;
      tile.style.gridColumnStart = col + 1;

      tile.dataset.row = row;
      tile.dataset.col = col;

      const label = labels[tileIndex];
      tile.textContent = label;
      tile.style.display = "flex";
      tile.style.alignItems = "center";
      tile.style.justifyContent = "center";
      tile.style.fontWeight = "bold";
      tile.style.fontSize = "16px";
      tile.style.color = "#fff";
      tile.style.textShadow = "1px 1px 2px #000";

      tile.addEventListener('click', () => handleTileClick(tile));
      tiles.push(tile);
      container.appendChild(tile);
    }
  });

function handleTileClick(tile) {
  const tileRow = parseInt(tile.dataset.row);
  const tileCol = parseInt(tile.dataset.col);

  const isAdjacent =
    (tileRow === emptyPosition.row && Math.abs(tileCol - emptyPosition.col) === 1) ||
    (tileCol === emptyPosition.col && Math.abs(tileRow - emptyPosition.row) === 1);

  if (isAdjacent) {
    tile.style.gridRowStart = emptyPosition.row + 1;
    tile.style.gridColumnStart = emptyPosition.col + 1;
    tile.dataset.row = emptyPosition.row;
    tile.dataset.col = emptyPosition.col;
    emptyPosition = { row: tileRow, col: tileCol };
  }
}

document.getElementById('validationForm').addEventListener('submit', function (e) {
  const tiles = Array.from(document.querySelectorAll('.tile'));
  tiles.sort((a, b) => {
    const rowA = parseInt(a.dataset.row);
    const rowB = parseInt(b.dataset.row);
    if (rowA !== rowB) return rowA - rowB;
    return parseInt(a.dataset.col) - parseInt(b.dataset.col);
  });

  let order = [];
  tiles.forEach(tile => {
    order.push(tile.textContent);
  });

  const solutionString = order.join('-');

  document.getElementById('solutionInput').value = solutionString;
  document.getElementById('signatureInput').value = puzzleSignature;
});
