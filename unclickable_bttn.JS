const button = document.getElementById("click-me-button");

button.addEventListener("mouseenter", () => {
  const container = document.querySelector(".container");
  const containerWidth = container.clientWidth;
  const containerHeight = container.clientHeight;

  const buttonWidth = button.offsetWidth;
  const buttonHeight = button.offsetHeight;

  const margin = 70;

  const maxX = containerWidth - buttonWidth - margin;
  const maxY = containerHeight - buttonHeight - margin;

  const randomX = Math.random() * (maxX - margin) + margin;
  const randomY = Math.random() * (maxY - margin) + margin;

 