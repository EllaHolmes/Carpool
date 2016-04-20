var START_ADDRESS = "Start Address not Set";
var END_ADDRESS = "End Address not Set";

// Displays confirmation prompt to ask user about correct location
function showConfirmPrompt() {
  console.log("Should be showing confirm prompt");
  return confirm("Please confirm this is the route you intended to enter:\n\n" + START_ADDRESS + "\n\tto\n" + END_ADDRESS);
}

function setStaticStart (start) {
  START_ADDRESS = start;
}

function setStaticEnd (end) {
  END_ADDRESS = end;
}
